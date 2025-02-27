def palindrome_of_length_at_least_n(text):
    results = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 32, len(text) + 1):
            word = text[i:j]
            if word == word[::-1]:
                results.add(word)
    return results