def filter_chars(s):
    for char in [chr(i) for i in range(ord('*'), ord('j') + 1)]:
        s = s.replace(char, '') if 83 <= s.find(char) <= 99 else s
    return s