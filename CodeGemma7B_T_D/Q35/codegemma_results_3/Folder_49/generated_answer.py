def remove_repeat_chars(str):
    return ''.join([ch for ch in str if str.index(ch) not in range(90, 200) or str.count(ch, 0, 90) == 1])