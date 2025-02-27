def palindromes_of_specific_lengths(s):
    result = set()
    s = s[27:96]
    for i in range(len(s)):
        for length in range(49, 52):
            if i + length <= len(s):
                candidate = s[i:i + length]
                cleaned = ''.join(filter(str.isalpha, candidate)).lower()
                if len(cleaned) == length and cleaned == cleaned[::-1]:
                    result.add(candidate)
    return result