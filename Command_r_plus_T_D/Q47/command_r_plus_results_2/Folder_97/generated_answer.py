def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[27:95].lower()
    palindromes = set()
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes