def remove_repeat_chars(s):
    chars_set = set()
    new_string_list = []
    for char in s:
        if 13 <= s.index(char) <= 76 and char not in chars_set:
            chars_set.add(char)
            new_string_list.append(char)
        if not 13 <= s.index(char) <= 76 and char in chars_set:
            chars_set.remove(char)
            new_string_list.remove(char)
    return ''.join(new_string_list)