def insert_after_character(text):
    words = text.split()
    result = []
    for word in words:
        new_word = []
        for char in word:
            new_word.append(char)
            if char == 's':
                new_word.append('w')
        result.append(''.join(new_word))
    return ' '.join(result)