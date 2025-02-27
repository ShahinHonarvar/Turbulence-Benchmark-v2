import itertools
    import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alpha = set(string.ascii_lowercase)
    result = set()
    for length in range(27, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if set(sub).issubset(alpha) and sub == sub[::-1]:
                result.add(sub)
    return result