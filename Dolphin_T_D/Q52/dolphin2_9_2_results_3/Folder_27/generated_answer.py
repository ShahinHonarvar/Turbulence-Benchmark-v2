def palindrome_of_length_n(s):
    s = s.lower()
    subs = {s[i:i + 56] for i in range(len(s) - 56 + 1)}
    return set(filter(lambda p: p == p[::-1], subs))