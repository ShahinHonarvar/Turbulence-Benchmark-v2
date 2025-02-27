def palindromes_of_specific_lengths(text):
    result = set()
    for index in range(18, 89):
        for length in range(12, 15):
            substring = text[index - length + 1:index + 1].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result