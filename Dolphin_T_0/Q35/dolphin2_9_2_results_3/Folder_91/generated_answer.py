def remove_repeat_chars(string):
    char_count = {}
    for char in string[:7]:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    altered_string = []
    for char in string:
        if char not in char_count or char_count[char] == 1:
            altered_string.append(char)
    return ''.join(altered_string)