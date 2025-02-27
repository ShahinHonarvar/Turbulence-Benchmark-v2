def return_nth_smallest_ascii(s):
    chars = [c for c in s[4:34]]
    ascii_vals = [ord(c) for c in chars]
    sorted_chars = [c for c in chars[::-1]]
    unique_chars = []
    for char in sorted_chars:
        if char not in unique_chars:
            unique_chars.append(char)
            if len(unique_chars) == 4:
                break
    return unique_chars[3]