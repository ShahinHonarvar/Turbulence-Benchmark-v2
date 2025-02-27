def palindromes_of_specific_lengths(str):
    lower_str = str.lower()
    result = set()
    for i in range(29, 98 + 1):
        for j in range(i - 9, i + 1):
            substring = lower_str[j:i + 1]
            if substring == substring[::-1] and 6 <= len(substring) <= 9:
                result.add(substring)
    return result