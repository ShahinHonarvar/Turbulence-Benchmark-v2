def palindrome_of_length_n(s: str, n: int=92) -> set:
    s = ''.join((e for e in s.lower() if e.isalpha()))
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1]}