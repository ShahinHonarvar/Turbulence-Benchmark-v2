def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[41:90]
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 39, len(substring) + 1)):
            substr = substring[i:j]
            cleaned = ''.join((c.lower() for c in substr if c.isalpha()))
            if cleaned == cleaned[::-1] and 23 <= len(cleaned) <= 38:
                result.add(cleaned)
    return result