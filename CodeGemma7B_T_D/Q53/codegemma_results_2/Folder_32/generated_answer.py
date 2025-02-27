def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 69, len(text)):
            word = text[i:j + 1].lower()
            if word == word[::-1]:
                result.add(text[i:j + 1])
    return result