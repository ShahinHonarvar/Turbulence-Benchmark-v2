def palindrome_of_length_at_least_n(text):
    length = len(text)
    result = set()
    for i in range(length - 31):
        for j in range(i + 1, length - 31):
            for k in range(j + 1, length):
                if text[i] == text[j].lower() == text[k].lower():
                    result.add(''.join(text[i:k + 1]))
    return result