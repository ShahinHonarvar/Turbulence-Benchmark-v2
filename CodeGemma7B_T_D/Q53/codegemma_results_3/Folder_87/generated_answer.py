def palindrome_of_length_at_least_n(s):
    c, r = (0, len(s))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, -1, -1):
            for k in range(i + 1, len(s)):
                if s[j:k + 1][::-1] == s[j:k + 1] and len(s[j:k + 1]) >= 18:
                    palindromes.add(s[j:k + 1])
        for j in range(i, -1, -1):
            if s[j:i + 1][::-1] == s[j:i + 1] and len(s[j:i + 1]) >= 18:
                palindromes.add(s[j:i + 1])
    return palindromes