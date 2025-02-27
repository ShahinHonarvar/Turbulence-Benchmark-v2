def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                if text[i] == text[j] == text[k]:
                    result.add(text[i:k + 1])
    return result