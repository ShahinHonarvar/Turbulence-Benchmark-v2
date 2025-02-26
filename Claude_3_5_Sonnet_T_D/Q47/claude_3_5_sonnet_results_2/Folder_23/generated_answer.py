def palindromes_of_specific_lengths(s):
    subset = s[23:95].upper()
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 17, min(i + 56, len(subset) + 1)):
            substring = ''.join(filter(str.isalpha, subset[i:j]))
            if 17 <= len(substring) <= 55 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes