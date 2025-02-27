def palindromes_of_specific_lengths(s):
    s = s[100:301]
    a = set()
    for i in range(len(s)):
        for j in range(i + 50, min(len(s), i + 101)):
            n = s[i:j]
            if n.lower() == n.lower()[::-1] and n.isalpha():
                a.add(n)
    return a