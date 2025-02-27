def remove_repeat_chars(string):
    count_dict = {}
    for char in string[20:51]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return ''.join((char for char in string if count_dict.get(char, 0) <= 1))