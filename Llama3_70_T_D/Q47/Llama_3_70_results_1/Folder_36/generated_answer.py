def palindromes_of_specific_lengths(text):
    result = set()
    text = text.lower()
    for i in range(124, 283):
        for j in range(i + 115, min(i + 135, 284)):
            substring = text[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result