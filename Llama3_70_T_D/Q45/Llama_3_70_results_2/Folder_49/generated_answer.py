def palindromes_between_indices(s):
    s = s[5:8].lower()
    a, b, c = s
    return {a + b + a, a + c + a, b + a + b, b + c + b, c + a + c, c + b + c} if a == b == c else {a + b + a, b + a + b} if a == b else {c + b + c, b + c + b} if b == c else {c + a + c, a + c + a} if a == c else set()