def return_nth_smallest_ascii(s):
    start_index = 20
    end_index = 80
    sorted_chars = sorted(s[start_index:end_index + 1], key=lambda c: ord(c))
    return sorted_chars[10]