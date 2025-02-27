def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(40, 95):
        for j in range(45, 52):
            substring = text[i:i + j]
            if substring == substring[::-1]:
                result.add(substring)
    return result