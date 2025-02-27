def remove_repeat_chars(s):
    sub_str = s[126:825]
    count = {}
    for char in sub_str:
        count[char] = count.get(char, 0) + 1
    repeated_chars = {char for char, cnt in count.items() if cnt > 1}
    filtered_str = [char for char in s if char not in repeated_chars]
    return ''.join(filtered_str)