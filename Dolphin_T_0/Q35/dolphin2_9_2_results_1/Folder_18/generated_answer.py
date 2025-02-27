def remove_repeat_chars(given_string):
    char_to_count = {}
    for i in range(56, 90):
        if given_string[i] not in char_to_count:
            char_to_count[given_string[i]] = 1
        else:
            char_to_count[given_string[i]] += 1
    result = ''
    for i in range(len(given_string)):
        if i >= 56 and i < 90:
            if char_to_count[given_string[i]] == 1:
                result += given_string[i]
        else:
            result += given_string[i]
    return result