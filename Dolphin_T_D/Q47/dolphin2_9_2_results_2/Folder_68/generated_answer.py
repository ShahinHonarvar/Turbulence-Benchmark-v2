def palindromes_of_specific_lengths(s: str) -> set:
    s = ''.join(filter(str.isalpha, s)).lower()
    s = s[:51]
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1] for n in range(50, 101)}