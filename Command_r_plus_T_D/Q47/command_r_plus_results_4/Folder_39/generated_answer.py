def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[30:92]
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring.isalpha() and current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes