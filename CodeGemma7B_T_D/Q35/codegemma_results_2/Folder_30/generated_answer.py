def remove_repeat_chars(str):
    return ''.join((char for char, count in collections.Counter(str).items() if count == 1 or 23 <= str.index(char) < 24))