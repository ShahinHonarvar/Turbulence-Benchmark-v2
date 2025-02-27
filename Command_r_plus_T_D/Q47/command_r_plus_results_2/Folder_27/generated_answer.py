def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[12:100].lower()
    for i in range(len(substring) - 25):
        for length in range(26, 30):
            if i + length > len(substring) or not substring[i:i + length].isalpha() or substring[i:i + length] == substring[i:i + length][::-1]:
                continue
            palindromes.add(substring[i:i + length])
    return palindromes