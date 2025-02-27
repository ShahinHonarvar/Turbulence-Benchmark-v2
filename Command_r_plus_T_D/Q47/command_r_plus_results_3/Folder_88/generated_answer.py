def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[10:88].lower()
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length > len(substring):
                break
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes