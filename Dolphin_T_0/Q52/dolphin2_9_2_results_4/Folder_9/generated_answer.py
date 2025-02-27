def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 71):
        subs = s[i:i + 72]
        if subs == subs[::-1]:
            if subs.isalpha():
                palindromes.add(subs)
    return palindromes