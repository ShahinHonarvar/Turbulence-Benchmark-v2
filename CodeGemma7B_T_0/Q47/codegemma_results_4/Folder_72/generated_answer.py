def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    for i in range(26, 91):
        for j in range(i - 26, i + 27):
            if j - i + 1 in range(27, 59):
                if text[i - j + 26:i + 1] == text[i - j + 26:i + 1][::-1]:
                    result.add(text[i - j + 26:i + 1])
    return result