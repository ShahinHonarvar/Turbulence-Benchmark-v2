def remove_repeat_chars(s):
    count_dict = {}
    for i in range(35, 64):
        if i < len(s):
            if s[i] in count_dict:
                count_dict[s[i]] += 1
            else:
                count_dict[s[i]] = 1
    remove_chars = [char for char in count_dict if count_dict[char] > 1]
    result = ''
    for char in s:
        if char not in remove_chars:
            result += char
    return result