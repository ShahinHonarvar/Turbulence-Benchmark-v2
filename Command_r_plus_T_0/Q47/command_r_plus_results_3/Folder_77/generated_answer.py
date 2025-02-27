def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[102:277].lower()
    for length in range(100, 170):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes