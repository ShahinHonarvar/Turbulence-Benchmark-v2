def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindrome_set = set()
    s = s[2:6]
    for i in range(5, len(s) + 1):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            pal = ''.join(sorted(sub.lower()))
            for p in is_palindrome(pal):
                palindrome_set.add(p)
    return palindrome_set if palindrome_set else ''