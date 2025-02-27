def palindrome_of_length_n(s: str) -> set:
    n = 401
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if n > len(s):
        return set()
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1]}