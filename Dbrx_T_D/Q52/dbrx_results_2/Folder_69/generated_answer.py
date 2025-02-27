def palindrome_of_length_n(s: str) -> set:
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 472:
        return set()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i, min(len(s), i + 472) + 1) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}
    return {p for p in palindromes if len(p) == 472}