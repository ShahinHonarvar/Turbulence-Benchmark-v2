def return_nth_smallest_ascii(s):
    sorted_chars = [ch for ch in s[1:32] if 1 <= s.index(ch) <= 31]
    sorted_chars.sort(key=lambda x: ord(x))
    return sorted_chars[5]