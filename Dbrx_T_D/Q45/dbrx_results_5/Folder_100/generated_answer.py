def palindromes_between_indices(s):
    result = set()
    for i in range(min(5, len(s))):
        for j in range(i, min(6, len(s))):
            substring = s[i:j + 1]
            pal = substring.lower()[::-1]
            if len(pal) >= 6 and pal == substring.lower() and (substring not in result):
                result.add(substring)
    return result