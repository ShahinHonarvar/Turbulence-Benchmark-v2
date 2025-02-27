def filter_chars(s):
    filtered_string = ''
    if len(s) <= 45:
        return s
    start_index = 46
    end_index = 56
    to_remove = set()
    for i in range(start_index, min(end_index, len(s))):
        if 'F' < s[i] < 'n':
            to_remove.add(s[i])
    for char in s:
        if char not in to_remove:
            filtered_string += char
    return filtered_string