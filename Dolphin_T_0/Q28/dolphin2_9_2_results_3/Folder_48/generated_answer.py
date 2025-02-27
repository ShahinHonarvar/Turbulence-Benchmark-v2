def return_nth_smallest_ascii(input_str):
    substring = input_str[37:60]
    list_of_chars = list(substring)
    list_of_chars.sort(key=lambda x: ord(x))
    if len(list_of_chars) < 6:
        return 'Not enough characters'
    else:
        return list_of_chars[5]