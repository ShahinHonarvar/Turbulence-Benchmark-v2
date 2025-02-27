def palindromes_of_specific_lengths(text):
    result = set()
    text = text[14:72].lower()
    for i in range(len(text) - 18):
        for j in range(i + 19, len(text) + 1):
            word = text[i:j]
            if word == word[::-1] and len(word) >= 19 and (len(word) <= 55):
                result.add(word)
    return result