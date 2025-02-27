def remove_repeat_chars(s):
    count_dict = {}
    for i in range(2, 8):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
    repeat_chars = [char for char, count in count_dict.items() if count > 1]
    return ''.join([c for c in s if c not in repeat_chars])