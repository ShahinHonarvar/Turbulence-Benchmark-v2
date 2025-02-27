def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(3, 300):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i]
            substring = substring.lower()
            if substring == substring[::-1] and len(substring) <= 300 and (len(substring) >= 30):
                result.add(substring)
    return result