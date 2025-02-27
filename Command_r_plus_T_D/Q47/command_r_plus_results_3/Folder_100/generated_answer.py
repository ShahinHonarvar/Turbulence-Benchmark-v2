def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[29:97].lower()
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes