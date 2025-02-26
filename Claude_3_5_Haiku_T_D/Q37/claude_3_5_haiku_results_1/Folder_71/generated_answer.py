def filter_chars(s):
    chars_to_remove = set()
    for i in range(32, 47):
        if 0 <= ord(s[i]) - ord('0') <= ord('k') - ord('0'):
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))