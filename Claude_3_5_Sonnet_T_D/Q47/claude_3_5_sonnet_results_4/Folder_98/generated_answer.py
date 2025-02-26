def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    substring = s[:21]
    for i in range(len(substring)):
        for j in range(i + 5, min(i + 81, len(substring) + 1)):
            if j - i > 80:
                break
            substr = substring[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result