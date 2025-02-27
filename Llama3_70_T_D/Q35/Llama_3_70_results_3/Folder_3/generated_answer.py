def remove_repeat_chars(s):
    counter = {}
    for char in s[56:88]:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    repeat_chars = [char for char, count in counter.items() if count > 1]
    return ''.join([char for char in s if char not in repeat_chars])