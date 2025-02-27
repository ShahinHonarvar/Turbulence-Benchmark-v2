def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 137
    return set(filter(lambda p: len(p) >= n and p == p[::-1], ''.join((c for c in s if c.isalpha())).split()))