def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[:7].lower()
    for length in range(3, 7):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes