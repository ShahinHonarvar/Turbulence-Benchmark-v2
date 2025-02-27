def remove_repeat_chars(string):
    counts = [string[i:i + 2].count() for i in range(len(string) - 1)]
    for i in range(20, 35):
        if counts[i] > 1:
            string = string.replace(string[i], '')
    return string