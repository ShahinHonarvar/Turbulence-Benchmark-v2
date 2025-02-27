def palindromes_of_specific_lengths(s):
    result = set()
    s = s[15:87]
    for length in range(51, 61):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                result.add(sub)
    return result