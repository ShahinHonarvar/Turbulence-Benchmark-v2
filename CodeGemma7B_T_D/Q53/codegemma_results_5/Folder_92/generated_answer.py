def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 9):
        for j in range(i + 5, len(text)):
            if text[i:j + 1].lower() == text[i:j + 1][::-1].lower():
                result.add(text[i:j + 1])
    return result