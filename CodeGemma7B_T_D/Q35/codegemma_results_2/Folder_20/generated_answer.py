def remove_repeat_chars(word):
    for i in range(27, 97):
        while word.count(chr(i)) > 1:
            while chr(i) in word:
                word = word.replace(chr(i) + chr(i), chr(i))
    return word