def palindrome_of_length_at_least_n(s):
    return {x for x in [s[i:j + 1] for i in range(len(s)) for j in range(i, len(s))] if x.lower() == x[::-1].lower() and len(x) >= 63}