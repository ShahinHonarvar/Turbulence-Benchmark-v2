def remove_repeat_chars(s):
    s_200_202 = s[200:202]
    char_count = {}
    for char in s_200_202:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    result = ''.join([char for char in s if char not in repeat_chars])
    return result