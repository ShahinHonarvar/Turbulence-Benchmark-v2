def palindromes_of_specific_lengths(text):
    result = set()
    text = text.lower()
    for i in range(26, 91):
        for j in range(i + 27, 59):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                result.add(text[i:j + 1])
    return result