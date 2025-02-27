def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 95):
        subs = s[i:i + 96]
        if subs == subs[::-1]:
            palindromes.add(subs)
    return palindromes