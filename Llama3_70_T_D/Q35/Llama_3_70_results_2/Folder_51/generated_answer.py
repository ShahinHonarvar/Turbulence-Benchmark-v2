def remove_repeat_chars(s):
    count = {}
    for char in s[6:9]:
        count[char] = count.get(char, 0) + 1
    repeat_chars = [char for char, freq in count.items() if freq > 1]
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result