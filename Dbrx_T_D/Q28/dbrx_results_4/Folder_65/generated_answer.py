def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 32 <= ord(char) <= 67]
    sorted_chars = sorted(filtered_chars)
    try:
        return sorted_chars[12]
    except IndexError:
        return None