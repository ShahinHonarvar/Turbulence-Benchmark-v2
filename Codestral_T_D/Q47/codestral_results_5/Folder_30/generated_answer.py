def palindromes_of_specific_lengths(s):
    s = s[14:91]
    palindromes = set()
    for i in range(len(s)):
        for j in range(55, 72):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub.lower())
    return palindromes