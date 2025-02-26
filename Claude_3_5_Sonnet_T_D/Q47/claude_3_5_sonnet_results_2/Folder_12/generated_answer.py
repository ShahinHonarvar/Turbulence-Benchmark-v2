def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 22, len(substring) + 1)):
            substr = substring[i:j]
            cleaned = ''.join((c for c in substr if c.isalpha()))
            if 18 <= len(cleaned) <= 21 and cleaned.lower() == cleaned.lower()[::-1]:
                result.add(cleaned)
    return result