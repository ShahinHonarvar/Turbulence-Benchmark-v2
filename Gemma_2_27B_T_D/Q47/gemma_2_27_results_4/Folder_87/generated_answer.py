def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(11, 94):
        for j in range(i + 33, min(i + 54, 94)):
            substring = text[i:j + 1]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result