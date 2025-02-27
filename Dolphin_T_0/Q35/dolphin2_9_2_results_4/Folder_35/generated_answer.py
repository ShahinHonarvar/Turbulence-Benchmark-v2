def remove_repeat_chars(string):
    unused_chars = list(string)
    for i in range(77, 84):
        if string.count(string[i]) > 1:
            unused_chars = [c for c in unused_chars if c != string[i]]
    result = ''.join(unused_chars)
    return result