def remove_repeat_chars(s):
    count_dict = {}
    for i in range(90, 200):
        if i < len(s):
            char = s[i]
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    repeat_chars = set()
    for char, count in count_dict.items():
        if count > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])