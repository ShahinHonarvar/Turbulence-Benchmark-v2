def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[26:96].lower()
    palindromes = set()
    for i in range(len(substring) - 49):
        for length in range(49, 52):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes