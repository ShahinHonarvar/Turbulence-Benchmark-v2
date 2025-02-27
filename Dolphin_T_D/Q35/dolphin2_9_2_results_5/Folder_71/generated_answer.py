def remove_repeat_chars(string):
    chars = [char for char in string if string.count(char) == 1 and 20 <= string.index(char) <= 35]
    string = ''.join([char for char in string if char not in chars])
    return string