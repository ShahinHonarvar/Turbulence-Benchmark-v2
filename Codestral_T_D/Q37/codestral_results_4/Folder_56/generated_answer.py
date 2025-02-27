def filter_chars(s):
    chars = [chr(i) for i in range(ord('K'), ord('a') + 1)]
    return ''.join((char for i, char in enumerate(s) if not (71 <= i <= 94 and char in chars)))