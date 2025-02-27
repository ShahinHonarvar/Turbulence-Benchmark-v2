def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('A') + 1, ord('Q'))]
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 50 or s.index(char) > 92))