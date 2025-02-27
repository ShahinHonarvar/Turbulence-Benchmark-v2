def palindromes_of_specific_lengths(s):
    s = s[32:72]
    result = set()
    for len_ in range(21, 33):
        for i in range(len(s) - len_ + 1):
            sub = s[i:i + len_]
            if sub[::-1].lower() == sub.lower():
                result.add(sub)
    return result