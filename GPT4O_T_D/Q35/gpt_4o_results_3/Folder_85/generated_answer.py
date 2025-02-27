def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    counter = {}
    for char in s[2:8]:
        counter[char] = counter.get(char, 0) + 1
    chars_to_remove = {char for char, count in counter.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))