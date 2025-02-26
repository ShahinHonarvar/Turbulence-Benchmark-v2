def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[36:93]
    cleaned = ''.join((char.lower() for char in substring if char.isalpha()))
    n = len(cleaned)
    for i in range(n):
        for j in range(i + 10, min(i + 36, n + 1)):
            substring = cleaned[i:j]
            if substring == substring[::-1] and 10 <= len(substring) <= 35:
                result.add(substring)
    return result