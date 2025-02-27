def remove_repeat_chars(s):
    count_dict = {}
    repeat_chars = set()
    for char in s[36:52]:
        if char in count_dict:
            count_dict[char] += 1
            repeat_chars.add(char)
        else:
            count_dict[char] = 1
    return ''.join([char for char in s if char not in repeat_chars])