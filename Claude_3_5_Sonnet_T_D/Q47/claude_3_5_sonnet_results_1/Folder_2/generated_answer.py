def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:60]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 37, len(substring) + 1)):
            if j - i > 36:
                break
            current = substring[i:j]
            if current == current[::-1]:
                result.add(current)
    return result