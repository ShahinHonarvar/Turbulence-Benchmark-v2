def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 12):
        subs = s[i:i + 13]
        if subs == subs[::-1]:
            palindromes.add(subs)
    return palindromes