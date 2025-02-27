def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(18, 48):
        for i in range(43, 96):
            if i + length <= 96:
                sub = s[i:i + length]
                if sub == sub[::-1]:
                    result.add(sub)
    return result