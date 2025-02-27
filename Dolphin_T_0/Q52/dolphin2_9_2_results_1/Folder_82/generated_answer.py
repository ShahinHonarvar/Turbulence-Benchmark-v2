def palindrome_of_length_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 28, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                set_of_palindromes.add(subs)
    return set_of_palindromes