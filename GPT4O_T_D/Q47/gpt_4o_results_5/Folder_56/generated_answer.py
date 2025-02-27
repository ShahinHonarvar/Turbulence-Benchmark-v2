def palindromes_of_specific_lengths(s):
    s = s[1:10]
    result = set()
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            cleaned = ''.join(filter(str.isalpha, substr)).lower()
            if cleaned == cleaned[::-1] and len(cleaned) == length:
                result.add(substr)
    return result