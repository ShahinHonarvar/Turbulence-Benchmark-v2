def all_substring_of_size_n(str):
    windows = []
    n = 10
    for i in range(len(str) - n + 1):
        window = str[i:i + n]
        if window not in windows:
            windows.append(window)
    return windows