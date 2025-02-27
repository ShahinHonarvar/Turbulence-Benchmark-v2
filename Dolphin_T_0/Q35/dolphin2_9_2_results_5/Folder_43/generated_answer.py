def remove_repeat_chars(string):
    chars = [char for char in string[10:28]]
    repeat_chars = []
    for char in chars:
        if chars.count(char) > 1 and chars.count(char) not in repeat_chars:
            repeat_chars.append(chars.count(char))
    for char_count in repeat_chars:
        for i in range(len(string)):
            if string[i] == chars[char_count - 1]:
                string = string[:i] + string[i + 1:]
    return string