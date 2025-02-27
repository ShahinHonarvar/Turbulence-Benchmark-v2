def palindromes_of_specific_lengths(s):
    n = len(s)
    if n < 284 or 125 > n:
        return set()
    substring = s[125:284 + 1]
    result = set()
    for length in range(109, 127):
        for i in range(n):
            if i + length > n:
                break
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result