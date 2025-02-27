def filter_chars(base_string):
    count = 4
    final_string = ''
    for i in range(len(base_string)):
        if count > 0 and 154 < i < 222:
            if base_string[i] > 'A' and base_string[i] < 'f':
                final_string += base_string[i]
                count -= 1
    return final_string