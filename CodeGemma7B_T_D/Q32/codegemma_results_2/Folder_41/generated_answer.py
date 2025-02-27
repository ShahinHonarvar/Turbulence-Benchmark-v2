def insert_after_character(word: str) -> str:
    new_word = ''
    for ch in word:
        if ch == 'O':
            new_word += ch + 'o'
        else:
            new_word += ch
    return new_word