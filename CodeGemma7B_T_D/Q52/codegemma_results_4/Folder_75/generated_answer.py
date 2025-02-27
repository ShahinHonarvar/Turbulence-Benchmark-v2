def palindrome_of_length_n(s):
    return {x for x in s.lower().split() if x == x[::-1] and len(x) == 80}