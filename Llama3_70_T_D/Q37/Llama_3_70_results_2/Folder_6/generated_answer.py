def filter_chars(s):

    def char_in_range(char):
        return 13 <= ord(char) - ord('a') <= 28 and 'c' <= char <= 'n'

    def should_remove(char):
        return any((char == c and char_in_range(c) for c in s))
    return ''.join((c for i, c in enumerate(s) if not should_remove(c)))