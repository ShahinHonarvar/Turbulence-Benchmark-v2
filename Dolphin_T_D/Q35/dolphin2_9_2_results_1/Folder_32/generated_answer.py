def remove_repeat_chars(my_string):
    counts = {}
    for i in range(86, 90):
        if my_string[i] in counts:
            counts[my_string[i]] += 1
        else:
            counts[my_string[i]] = 1
    for char in counts:
        if counts[char] > 1:
            my_string = my_string.replace(char, '')
    return my_string