def remove_repeat_chars(s):
    sub_str = s[71:98]
    counter = {}
    for char in sub_str:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    repeated_chars = {char for char, count in counter.items() if count > 1}
    result = [char for char in s if char not in repeated_chars or s.index(char) <= 70 or s.index(char) >= 98]
    return ''.join(result)