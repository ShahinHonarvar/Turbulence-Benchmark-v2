def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 22, len(substring) + 1)):
            substr = substring[i:j]
            filtered = ''.join((c for c in substr if c.isalpha()))
            if filtered == filtered[::-1] and filtered.isalpha() and (18 <= len(filtered) <= 21):
                result.add(filtered.lower())
    return result