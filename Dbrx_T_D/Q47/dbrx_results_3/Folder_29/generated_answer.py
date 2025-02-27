def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    for length in range(18, 74):
        for start_index in range(15, 95 - length):
            substring = s[start_index:start_index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes