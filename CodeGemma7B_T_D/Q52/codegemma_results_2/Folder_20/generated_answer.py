def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 52):
        for j in range(i + 1, len(text) - 51):
            if text[i:j + 1].lower().replace(' ', '') == text[j:j + 53][::-1].lower().replace(' ', ''):
                result.add(text[i:j + 53])
    return result