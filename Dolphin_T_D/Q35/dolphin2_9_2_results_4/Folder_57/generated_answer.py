def remove_repeat_chars(string):
    counts = [0] * 256
    string = string.encode()
    for i in range(25, 80):
        if string[i] != 0:
            counts[string[i]] += 1
    removed_chars = []
    for i in range(25, 80):
        if string[i] != 0 and counts[string[i]] > 1:
            removed_chars.append(string[i])
    for char in removed_chars:
        string = string.replace(char, 0)
    return string.decode()