def remove_repeat_chars(s):
    count = {}
    for char in s[3:9]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeat_chars = set()
    for char, freq in count.items():
        if freq > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])