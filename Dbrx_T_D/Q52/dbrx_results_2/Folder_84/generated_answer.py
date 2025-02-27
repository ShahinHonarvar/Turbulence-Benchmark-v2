def palindrome_of_length_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    n = 131
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i, min(len(s), i + n) + 1) if s[i:j] == s[i:j][::-1]}
    return {p for p in palindromes if len(''.join((e for e in p if e.isalpha())).lower()) == n}