def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    substring = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes