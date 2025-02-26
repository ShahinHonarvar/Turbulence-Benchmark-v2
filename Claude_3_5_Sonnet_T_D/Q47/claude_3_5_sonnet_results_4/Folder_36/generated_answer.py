def palindromes_of_specific_lengths(s):
    substring = s[124:284]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 115, min(i + 135, len(substring) + 1)):
            substr = substring[i:j]
            cleaned = ''.join((c for c in substr if c.isalpha()))
            if cleaned == cleaned[::-1] and 115 <= len(cleaned) <= 134:
                result.add(cleaned.lower())
    return result