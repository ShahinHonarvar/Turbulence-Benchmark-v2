def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    result = set()
    for length in range(13, 67):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result