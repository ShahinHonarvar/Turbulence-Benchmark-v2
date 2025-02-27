def filter_chars(s):
    chars_to_remove = set()
    relevant_portion = s[384:412]
    for char in relevant_portion:
        if '/' <= char <= '8':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))