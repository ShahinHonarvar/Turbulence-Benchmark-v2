def palindromes_of_specific_lengths(s):
    s = s[119:256]
    result = set()
    for length in range(104, 124):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                result.add(sub.lower())
    return result