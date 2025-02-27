def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[18:88]
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes