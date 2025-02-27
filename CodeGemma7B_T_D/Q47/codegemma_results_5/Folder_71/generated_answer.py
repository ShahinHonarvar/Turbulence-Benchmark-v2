def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(18, 65 + 1):
        for j in range(23, 36 + 1):
            middle = (j - 1) // 2
            start = i - middle
            end = i + middle + 1
            substring = text[start:end].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result