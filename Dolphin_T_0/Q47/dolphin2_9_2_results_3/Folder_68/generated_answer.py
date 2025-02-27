def palindromes_of_specific_lengths(s):
    result = set()
    s = s[0:51]
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result