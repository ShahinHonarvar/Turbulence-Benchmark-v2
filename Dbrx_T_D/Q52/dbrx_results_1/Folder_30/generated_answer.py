def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, min(len(s), i + 94)) if s[i:j] == s[i:j][::-1]}