def palindromes_of_specific_lengths(s):
    s = s[10:71]
    result = set()
    for length in range(24, 53):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result