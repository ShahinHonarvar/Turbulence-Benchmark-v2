def palindromes_of_specific_lengths(s):
    s = s[15:90]
    palindromes = set()
    for i in range(40, 73):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub.lower() and sub == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes