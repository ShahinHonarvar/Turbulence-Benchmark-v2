def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                word = text[i:j + 1] + text[j + 1:k + 2] + text[k + 2:i:-1]
                if word == word[::-1] and len(word) == 366:
                    result.add(word)
    if not result:
        return set()
    else:
        return result