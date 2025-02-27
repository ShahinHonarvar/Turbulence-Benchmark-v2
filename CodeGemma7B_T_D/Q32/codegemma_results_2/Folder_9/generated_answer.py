def insert_after_character(word):
    return ''.join((insert_substring_after_character(c, 'e', 'E', word) for c in word))

def insert_substring_after_character(char, search_char, substring, word):
    if char != search_char:
        return char
    if substring == '':
        return char + substring
    return char + substring + ''.join((insert_substring_after_character(c, search_char, substring, word) for c in word))