def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    palindromes_set = set()
    for i in range(17, 56):
        for j in range(len(substring) - i + 1):
            if all((c.isalpha() for c in substring[j:j + i])) and substring[j:j + i].lower() == substring[j:j + i][::-1].lower():
                palindromes_set.add(substring[j:j + i])
    return palindromes_set