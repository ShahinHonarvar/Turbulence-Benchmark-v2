def remove_repeat_chars(s):
    count = {}
    chars_to_remove = set()
    for char in s[68:99]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        if count[char] > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])