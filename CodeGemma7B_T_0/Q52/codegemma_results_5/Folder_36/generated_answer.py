def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 337):
        for j in range(i + 1, len(text) - 336):
            for k in range(j + 1, len(text) - 335):
                if text[i:i + 338] == text[i + 338:i + 676][::-1]:
                    result.add(text[i:i + 338])
    return result