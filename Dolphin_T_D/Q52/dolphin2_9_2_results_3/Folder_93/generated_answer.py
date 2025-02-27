def palindrome_of_length_n(s):
    s = s.lower()
    set_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 45, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and subs.isalpha():
                set_palindromes.add(subs)
    return set_palindromes