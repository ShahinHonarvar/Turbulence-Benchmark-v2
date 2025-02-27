def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(6, 9):
        for j in range(10, 75):
            if s[j:j + i].lower() == s[j:j + i].lower()[::-1] and s[j:j + i].lower().isalpha():
                result.add(s[j:j + i])
    return result