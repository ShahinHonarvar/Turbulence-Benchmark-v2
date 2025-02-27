def remove_repeat_chars(string):
    count = {}
    for i in range(462, 995):
        if string[i] in count:
            count[string[i]] += 1
        else:
            count[string[i]] = 1
    repeat_chars = [char for char, freq in count.items() if freq > 1]
    new_string = ''
    for char in string:
        if char not in repeat_chars:
            new_string += char
    return new_string