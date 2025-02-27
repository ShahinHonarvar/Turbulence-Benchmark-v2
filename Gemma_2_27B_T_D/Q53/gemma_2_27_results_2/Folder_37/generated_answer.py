def palindrome_of_length_at_least_n(s):
    return {p for p in set([s[i:j + 1].lower() for i in range(len(s)) for j in range(i, len(s))]) if len(p) >= 67 and p == p[::-1]}