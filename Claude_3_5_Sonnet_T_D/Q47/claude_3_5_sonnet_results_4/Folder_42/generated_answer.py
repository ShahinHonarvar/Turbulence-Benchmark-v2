def palindromes_of_specific_lengths(s):
    substring = s[43:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 48, len(substring) + 1)):
            substr = substring[i:j]
            clean_substr = ''.join((c for c in substr if c.isalpha()))
            if len(clean_substr) >= 18 and len(clean_substr) <= 47:
                if clean_substr.lower() == clean_substr.lower()[::-1]:
                    result.add(clean_substr)
    return result