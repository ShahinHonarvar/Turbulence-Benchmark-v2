def remove_repeat_chars(s):
    count_dict = {}
    for i in range(18, 60):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
    repeat_chars = [char for char, count in count_dict.items() if count > 1]
    return ''.join([char for char in s if char not in repeat_chars])