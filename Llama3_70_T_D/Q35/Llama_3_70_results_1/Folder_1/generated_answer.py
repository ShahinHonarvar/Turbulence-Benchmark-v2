def remove_repeat_chars(s):
    count = {}
    for char in s[17:88]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    remove_chars = [char for char, num in count.items() if num > 1]
    return ''.join((char for char in s if char not in remove_chars))