def remove_repeat_chars(s):
    s_list = list(s)
    count = {}
    for i in range(126, 825):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for key, value in count.items():
        if value > 1:
            s_list = [char for char in s_list if char != key]
    return ''.join(s_list)