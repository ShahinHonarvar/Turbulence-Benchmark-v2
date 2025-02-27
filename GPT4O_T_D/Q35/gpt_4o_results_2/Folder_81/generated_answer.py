def remove_repeat_chars(s):
    count = {}
    filtered_part = s[21:200]
    for char in filtered_part:
        count[char] = count.get(char, 0) + 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    result = ''.join([char for char in s if char not in to_remove or s.index(char) <= 20 or s.index(char) >= 200])
    return result