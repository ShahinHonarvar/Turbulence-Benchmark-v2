def palindromes_of_specific_lengths(s):
    s = s[0:7].lower()
    palindromes = set()
    for length in range(3, 7):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if len(set(sub)) == 1 and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes