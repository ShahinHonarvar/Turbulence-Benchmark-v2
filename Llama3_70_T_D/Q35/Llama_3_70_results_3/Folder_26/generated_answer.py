def remove_repeat_chars(s):
    count_dict = {}
    for char in s[68:99]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    repeat_chars = [char for char in count_dict if count_dict[char] > 1]
    return ''.join([char for char in s if char not in repeat_chars])