def palindromes_of_specific_lengths(s):
    s = s[:21]
    pal = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(s)):
        for j in range(i + 4, len(s)):
            t = ''.join(filter(str.isalpha, s[i:j + 1]))
            t = t.lower()
            if is_palindrome(t) and 5 <= len(t) <= 80:
                pal.add(t)
    return pal