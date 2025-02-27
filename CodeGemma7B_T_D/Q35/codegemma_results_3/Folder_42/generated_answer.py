def remove_repeat_chars(str1):
    for character in str1[18:60]:
        if str1.count(character) > 1:
            str1 = str1.replace(character, '')
    return str1