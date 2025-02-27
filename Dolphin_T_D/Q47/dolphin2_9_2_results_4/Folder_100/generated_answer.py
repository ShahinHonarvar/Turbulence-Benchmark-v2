def palindromes_of_specific_lengths(s):
    s = s[29:97]
    result = set()
    for length in range(12, 19):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub[::-1].lower():
                result.add(sub)
    return result