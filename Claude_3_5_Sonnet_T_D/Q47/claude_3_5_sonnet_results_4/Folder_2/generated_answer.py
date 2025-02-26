def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:60]
    substring = ''.join((char.lower() for char in substring if char.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 37, len(substring) + 1)):
            if j - i > 36:
                break
            segment = substring[i:j]
            if segment == segment[::-1]:
                result.add(segment)
    return result