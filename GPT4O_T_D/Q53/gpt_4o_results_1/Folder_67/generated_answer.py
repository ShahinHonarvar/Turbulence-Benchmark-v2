def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def extract_letters(s):
        return ''.join((c for c in s if c.isalpha()))
    s = extract_letters(s.lower())
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 25, n + 1):
            subst = s[i:j]
            if is_palindrome(subst):
                result.add(subst)
    return result