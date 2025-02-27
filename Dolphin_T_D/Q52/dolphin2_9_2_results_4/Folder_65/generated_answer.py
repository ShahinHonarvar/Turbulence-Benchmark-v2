def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 34):
        subs = s[i:i + 35]
        if subs == subs[::-1] and all((char.isalpha() for char in subs)):
            palindromes.add(subs)
    return palindromes