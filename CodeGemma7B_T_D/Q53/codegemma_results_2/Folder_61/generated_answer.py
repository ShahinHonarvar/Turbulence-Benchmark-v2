def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            word = text[i:j + 1]
            if word == word[::-1] and 5 <= len(word) and word.isalpha():
                result.add(word.lower())
    return result