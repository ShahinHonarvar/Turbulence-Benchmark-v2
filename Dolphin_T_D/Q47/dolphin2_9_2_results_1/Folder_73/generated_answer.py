def palindromes_of_specific_lengths(s):
    subs = s[21:63]
    result = set()
    for length in range(22, 34):
        for i in range(len(subs) - length + 1):
            sub = subs[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result