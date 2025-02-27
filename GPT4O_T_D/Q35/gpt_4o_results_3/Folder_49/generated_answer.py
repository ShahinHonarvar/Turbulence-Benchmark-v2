def remove_repeat_chars(s):
    start, end = (91, 200)
    count = {}
    for i in range(start + 1, end):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeated_chars = {char for char, c in count.items() if c > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result