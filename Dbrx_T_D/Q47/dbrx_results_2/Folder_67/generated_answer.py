def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(65, 100):
        for j in range(26, 34):
            if i + j - 1 <= 99:
                substr = s[i:i + j].lower()
                if substr == substr[::-1] and substr.isalpha():
                    result.add(substr)
    return result