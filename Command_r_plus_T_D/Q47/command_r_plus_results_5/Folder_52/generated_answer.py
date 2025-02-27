def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes