def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[21:63]
    substr = ''.join((c for c in substr if c.isalpha()))
    substr = substr.lower()
    n = len(substr)
    for i in range(n):
        for j in range(i + 22, min(i + 34, n + 1)):
            segment = substr[i:j]
            if segment == segment[::-1] and 22 <= len(segment) <= 33:
                result.add(segment)
    return result