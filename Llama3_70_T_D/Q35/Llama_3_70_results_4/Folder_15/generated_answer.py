def remove_repeat_chars(s):
    count = {}
    for char in s[1:4]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    repeat_chars = [char for char in count if count[char] > 1]
    return ''.join([char for char in s if char not in repeat_chars])