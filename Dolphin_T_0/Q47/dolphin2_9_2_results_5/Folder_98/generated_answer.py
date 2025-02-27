def palindromes_of_specific_lengths(s):
    length = len(s)
    s = s[:21] if length > 21 else s
    result = set()
    for i in range(length - 2):
        for j in range(i + 5, min(i + 81, length + 1)):
            x = s[i:j]
            if x == x[::-1] and all((c.isalpha() for c in x)):
                result.add(x)
    return result