def palindromes_of_specific_lengths(s):
    s = s[17:73]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(50, 52):
            if i + j > len(s):
                break
            sub = s[i:i + j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes