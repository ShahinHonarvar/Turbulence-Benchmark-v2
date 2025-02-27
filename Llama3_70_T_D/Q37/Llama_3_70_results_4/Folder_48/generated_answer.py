def filter_chars(s):
    chars = [chr(i) for i in range(ord('?'), ord('n') + 1)]
    filtered_chars = [char for char in s if not (ord('?') <= ord(char) <= ord('n') and 513 <= s.index(char) <= 877)]
    return ''.join(filtered_chars)