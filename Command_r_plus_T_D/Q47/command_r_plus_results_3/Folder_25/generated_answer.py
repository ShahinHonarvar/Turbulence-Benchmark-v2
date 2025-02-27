def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[25:85]
    for length in range(30, 47):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes