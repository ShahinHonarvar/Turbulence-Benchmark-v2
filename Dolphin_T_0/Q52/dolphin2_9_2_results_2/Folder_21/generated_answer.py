def palindrome_of_length_n(s):
    s = s.lower()
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    n = 407
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i, len(s) - n + 1):
            subs = s[i:j + n]
            if set(subs).issubset(English_letters) and subs[::-1] == subs:
                palindromes.add(subs)
    return palindromes