def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[30:92]
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha() and substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes