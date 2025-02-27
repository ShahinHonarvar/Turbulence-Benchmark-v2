def palindromes_of_specific_lengths(s):
    s = s[10:56].lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 2, length + 1):
            sub = s[i:j]
            if sub == sub[::-1] and 3 <= len(sub) <= 7:
                palindromes.add(sub)
    return palindromes