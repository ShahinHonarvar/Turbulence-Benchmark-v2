def palindromes_of_specific_lengths(s):
    substring = s[70:141]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 61, len(substring) + 1)):
            substr = substring[i:j]
            cleaned = ''.join((c.lower() for c in substr if c.isalpha()))
            if cleaned == cleaned[::-1] and 3 <= len(cleaned) <= 60:
                result.add(cleaned)
    return result