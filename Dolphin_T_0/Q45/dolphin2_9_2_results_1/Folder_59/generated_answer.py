def palindromes_between_indices(s):
    palindromes = set()
    substring = s[8:10]
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            substring_i_j = substring[i:j]
            if substring_i_j == substring_i_j[::-1] and len(substring_i_j) >= 3:
                palindromes.add(substring_i_j.lower())
    return palindromes