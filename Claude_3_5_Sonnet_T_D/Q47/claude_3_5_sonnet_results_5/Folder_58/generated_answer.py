def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[125:284]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 109, min(i + 127, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and 109 <= len(substr) <= 126:
                result.add(substr)
    return result