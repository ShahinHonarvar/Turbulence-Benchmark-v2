def palindrome_of_length_at_least_n(s):
    s = s.lower()
    rev_s = s[::-1]
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 2, length + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes