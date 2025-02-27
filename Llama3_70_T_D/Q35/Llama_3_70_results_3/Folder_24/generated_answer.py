def remove_repeat_chars(s):
    s = list(s)
    count_dict = {}
    for char in s[13:91]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    for char in count_dict:
        if count_dict[char] > 1:
            s = [c for c in s if c != char]
    return ''.join(s)