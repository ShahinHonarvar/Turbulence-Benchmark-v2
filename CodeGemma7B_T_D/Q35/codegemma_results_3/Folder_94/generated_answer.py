def remove_repeat_chars(x):
    for i in range(42, 87):
        for j in range(i + 1, 87):
            if x[i] == x[j]:
                x = x[:j] + x[j + 1:]
                j -= 1
    return x