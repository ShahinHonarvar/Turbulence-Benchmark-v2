def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for len_ in range(3, len(s) + 1):
        for i in range(0, len(s) - len_ + 1):
            subs = s[i:i + len_]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes