def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[22:83].lower()
    for i in range(len(substring) - 33):
        for length in range(32, 35):
            if substring[i:i + length].isalpha() and substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes