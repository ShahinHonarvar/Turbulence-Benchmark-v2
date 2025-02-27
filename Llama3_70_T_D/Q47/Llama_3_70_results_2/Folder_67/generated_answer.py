def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[65:100]
    result = set()
    for length in range(26, 34):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result