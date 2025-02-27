def palindromes_of_specific_lengths(s):
    target = s[10:75].lower()
    result = set()
    for length in range(6, 9):
        for i in range(len(target) - length + 1):
            substring = target[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result