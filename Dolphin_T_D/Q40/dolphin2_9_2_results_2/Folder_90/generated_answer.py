def return_n_smallest_chars(s):
    chars = [char for char in s.replace(' ', '')]
    chars.sort(key=lambda c: ord(c), reverse=True)
    chars = chars[:24]
    return sorted(chars, key=lambda c: ord(c), reverse=True)