def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[8:66] if s.count(char) == 1]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None