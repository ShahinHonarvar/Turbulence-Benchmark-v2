def palindromes_of_specific_lengths(s):
    s = s[16:78]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 43, i + 48):
            if j > len(s):
                break
            sub = s[i:j]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes