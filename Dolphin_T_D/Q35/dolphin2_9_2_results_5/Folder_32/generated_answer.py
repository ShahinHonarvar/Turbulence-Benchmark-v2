def remove_repeat_chars(bracketed_string):
    count_dict = {}
    for i in range(87, 90):
        if bracketed_string[i] in count_dict:
            count_dict[bracketed_string[i]] += 1
        else:
            count_dict[bracketed_string[i]] = 1
    new_string = ''
    for char in bracketed_string:
        if char in count_dict and count_dict[char] <= 1:
            new_string += char
    return new_string