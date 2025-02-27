def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            t = s[i:j + 1]
            if t.lower() == t.lower()[::-1] and t.isalpha() and (len(t) >= 19):
                palindromes.add(t)
    return palindromes