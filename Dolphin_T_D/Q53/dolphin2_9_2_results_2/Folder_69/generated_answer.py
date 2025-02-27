def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 8, len(s)):
            subs = s[i:j + 1]
            if subs == subs[::-1] and len(subs) >= 98:
                palindromes.add(subs)
    return palindromes