def palindrome_of_length_at_least_n(s):
    s = s.lower()
    chars = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 41, len(s) + 1):
            subs = s[i:j]
            if all((char in chars for char in subs)) and subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes