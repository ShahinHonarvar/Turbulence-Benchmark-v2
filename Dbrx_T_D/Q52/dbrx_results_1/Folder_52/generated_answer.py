def palindrome_of_length_n(s: str) -> set:
    n = 423
    if len(s) < n:
        return set()
    s = s.lower()
    return {s[i:n + i] for i in range(len(s) - n + 1) if s[i:n + i] == s[i:n + i][::-1]}