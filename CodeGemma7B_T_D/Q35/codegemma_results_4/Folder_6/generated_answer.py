def remove_repeat_chars(str):
    string = str[0:20] + ''.join([ch for ch in str[20:93] if str[20:93].count(ch) == 1]) + str[93:]
    return string