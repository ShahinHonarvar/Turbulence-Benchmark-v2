def palindrome_of_length_n(s):
    s = s.lower()
    n = 289
    palindromes = set()
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if subs == subs[::-1]:
            palindromes.add(subs)
    return palindromes