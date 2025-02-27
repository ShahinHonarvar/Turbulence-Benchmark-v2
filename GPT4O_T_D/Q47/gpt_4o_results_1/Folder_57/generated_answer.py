def palindromes_of_specific_lengths(s):
    result = set()
    s = s[16:95].lower()
    for start in range(len(s)):
        for end in range(start + 39, min(start + 53, len(s) + 1)):
            substring = s[start:end]
            cleaned = ''.join(filter(str.isalpha, substring))
            if len(cleaned) >= 39 and cleaned == cleaned[::-1]:
                result.add(cleaned)
    return result