def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    if text[i:l + 1] == text[i:l + 1][::-1]:
                        result.add(text[i:l + 1])
    return result