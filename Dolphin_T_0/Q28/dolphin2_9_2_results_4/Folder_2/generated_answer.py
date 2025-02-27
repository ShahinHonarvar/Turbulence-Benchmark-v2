def return_nth_smallest_ascii(s):
    valid_chars = [ch for ch in s if 48 <= ord(ch) <= 76]
    valid_chars.sort(lambda x, y: ord(x) - ord(y))
    return valid_chars[4]