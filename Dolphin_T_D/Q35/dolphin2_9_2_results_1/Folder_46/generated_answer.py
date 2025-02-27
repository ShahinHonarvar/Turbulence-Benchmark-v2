def remove_repeat_chars(string):
    to_remove = {char for char in string[10:80] if string[10:80].count(char) > 1}
    return ''.join((char for char in string if char not in to_remove))