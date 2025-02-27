def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        if i + 44 < len(s):
            for j in range(i, len(s) - 43):
                w = s[j:j + 44]
                if w == w[::-1] and w.isalpha():
                    palindromes.add(w)
    return palindromes