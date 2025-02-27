def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[12:100].lower()
    for i in range(len(substring) - 25):
        for length in range(26, 30):
            if i + length <= len(substring) and substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes