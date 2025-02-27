def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[22:83].lower()
    palindromes = set()
    for i in range(len(substring) - 33):
        for length in range(32, 35):
            if i + length <= len(substring) and substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes