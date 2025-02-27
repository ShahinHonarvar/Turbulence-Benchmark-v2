def palindromes_of_specific_lengths(text):
    text = text.lower()
    output = set()
    for i in range(18, 88):
        for j in range(38, 61):
            for k in range(i - j + 1):
                if text[i - k:i + 1] == text[i - k:i + 1][::-1]:
                    output.add(text[i - k:i + 1])
    return output