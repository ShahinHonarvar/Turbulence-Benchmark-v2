def palindromes_of_specific_lengths(s):
    substring = s[:11]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1] and 3 <= len(sub) <= 5:
                palindromes.add(sub.lower())
    return palindromes