def palindromes_of_specific_lengths(s):
    s = s[15:90]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 39, len(s)):
            sub = s[i:j + 1]
            if len(sub) % 2 == 0 and sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
            elif len(sub) % 2 != 0 and sub[1:] == sub[1:][::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes