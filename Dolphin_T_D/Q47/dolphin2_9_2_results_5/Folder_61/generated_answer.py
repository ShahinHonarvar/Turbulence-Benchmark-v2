def palindromes_of_specific_lengths(s):
    substring = s[:31]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            sub = substring[i:j + 1]
            if 20 <= len(sub) <= 30 and sub == sub.lower() and (sub == sub[::-1]):
                palindromes.add(sub)
    return palindromes