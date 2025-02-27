def palindromes_of_specific_lengths(s):
    results = set()
    s = s[10:75]
    for length in range(6, 9):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                results.add(sub.lower())
    return results