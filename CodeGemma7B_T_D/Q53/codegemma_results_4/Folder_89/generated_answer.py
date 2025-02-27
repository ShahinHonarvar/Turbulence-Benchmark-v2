def palindrome_of_length_at_least_n(s):
    """
                :type s: str
                :rtype: set[str]
                """
    return {w for w in (s[i:j + 1].lower() for i in range(len(s)) for j in range(i, len(s))) if w[::-1] == w and len(w) >= 43}