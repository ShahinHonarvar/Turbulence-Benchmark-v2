def palindromes_of_specific_lengths(str):
    result = set()
    str = str.lower()
    for i in range(18, 88):
        for j in range(i - 38, i + 1):
            if j < 0 or j >= len(str):
                continue
            substring = str[j:i + 1]
            if substring == substring[::-1] and len(substring) >= 38 and (len(substring) <= 60):
                result.add(substring)
    return result