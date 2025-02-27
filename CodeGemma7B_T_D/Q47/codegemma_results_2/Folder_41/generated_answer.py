def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(1, 8):
        for j in range(i - 2, i + 2):
            if j >= 1 and j <= 7:
                sub = s[j:i + 1].lower()
                if sub == sub[::-1] and len(sub) % 2 in range(3, 5):
                    result.add(sub)
    return result