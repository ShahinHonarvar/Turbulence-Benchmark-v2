def filter_chars(word):
    for i in range(23, 89 + 1):
        for j in range(word.find(word[i]), len(word)):
            if word[j] == word[i]:
                word = word[:j] + word[j + 1:]
    return word