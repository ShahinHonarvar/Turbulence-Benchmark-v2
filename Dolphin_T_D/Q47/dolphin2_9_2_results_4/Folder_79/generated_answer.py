def palindromes_of_specific_lengths(s):
    s = s[1:9]
    result = set()
    for length in range(3, 5):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result