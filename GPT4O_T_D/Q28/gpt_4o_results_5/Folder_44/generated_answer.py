def return_nth_smallest_ascii(s):
    sub_range_chars = [char for i, char in enumerate(s) if 20 <= i <= 30]
    sub_range_chars.sort(key=lambda x: ord(x))
    return sub_range_chars[7] if len(sub_range_chars) >= 8 else None