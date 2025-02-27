def remove_repeat_chars(s):
    chars_to_remove = set()
    count_dict = {}
    for char in s[200:202]:
        if char in count_dict:
            count_dict[char] += 1
            chars_to_remove.add(char)
        else:
            count_dict[char] = 1
    return ''.join([char for char in s if char not in chars_to_remove])