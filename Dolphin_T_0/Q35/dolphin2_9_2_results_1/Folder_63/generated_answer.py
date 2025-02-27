def remove_repeat_chars(string):
    char_count = {}
    for char in string[81:86]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    altered_string = []
    for i in range(len(string)):
        char = string[i]
        if char not in char_count or char_count[char] == 1:
            altered_string.append(char)
    return ''.join(altered_string)