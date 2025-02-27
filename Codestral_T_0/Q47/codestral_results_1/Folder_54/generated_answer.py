def palindromes_of_specific_lengths(s):
    s = s[27:78]
    palindromes = set()
    for i in range(len(s)):
        for j in range(18, 20):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                    palindromes.add(sub)
    return palindromes