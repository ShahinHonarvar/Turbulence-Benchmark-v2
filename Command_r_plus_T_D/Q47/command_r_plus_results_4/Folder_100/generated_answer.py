def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[29:97]
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes