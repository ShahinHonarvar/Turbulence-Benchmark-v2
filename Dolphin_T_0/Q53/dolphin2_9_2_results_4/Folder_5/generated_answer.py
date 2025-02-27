def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alpha_s = ''.join((c for c in s if c.isalpha()))
    n = 46
    return {alpha_s[i:j] for i in range(len(alpha_s) - n + 1) for j in range(i + n, len(alpha_s) + 1) if alpha_s[i:j] == alpha_s[i:j][::-1]}