def remove_repeat_chars(word):
    for i in range(len(word)):
        if i >= 33 and i <= 78:
            for j in range(i + 1, len(word)):
                if word[j] == word[i]:
                    word = word[:j] + word[j + 1:]
                    j -= 1
    return word