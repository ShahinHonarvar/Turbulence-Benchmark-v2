def palindrome_of_length_n(s: str) -> set:
    s = ''.join((e for e in s if e.isalpha())).lower()
    n = 24
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i, len(s)) if s[i:j] == s[i:j][::-1] and len(s[i:j]) == n}
    return palindromes