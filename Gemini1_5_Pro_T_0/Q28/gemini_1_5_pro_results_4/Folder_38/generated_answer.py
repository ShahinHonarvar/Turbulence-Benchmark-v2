def return_nth_smallest_ascii(s):
    filtered_chars = [ord(char) for i, char in enumerate(s) if 0 <= i <= 45]
    sorted_chars = sorted(filtered_chars)
    if len(sorted_chars) >= 10:
        return chr(sorted_chars[9])
    else:
        return None