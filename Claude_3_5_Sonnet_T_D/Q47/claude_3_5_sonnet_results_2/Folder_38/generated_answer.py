def palindromes_of_specific_lengths(s):
    substring = s[18:88]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 38, min(i + 61, len(substring) + 1)):
            substr = substring[i:j]
            cleaned = ''.join((c for c in substr if c.isalpha()))
            if cleaned == cleaned[::-1] and cleaned.isalpha() and (38 <= len(cleaned) <= 60):
                result.add(cleaned.lower())
    return result