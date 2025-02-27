def palindromes_of_specific_lengths(s):
    s = s[21:63]
    result = set()
    for i in range(22, 34):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i].lower()
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result