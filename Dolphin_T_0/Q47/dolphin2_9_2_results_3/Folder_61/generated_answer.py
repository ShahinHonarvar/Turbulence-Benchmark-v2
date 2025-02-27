def palindromes_of_specific_lengths(s):
    s = s[:31]
    result = set()
    for len_ in range(20, 31):
        for i in range(len_ - 1, len(s) - len_ + 1):
            sub = s[i - len_ + 1:i + len_]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result