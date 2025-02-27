def palindromes_of_specific_lengths(s: str) -> set:
    s = s[18:99]
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes