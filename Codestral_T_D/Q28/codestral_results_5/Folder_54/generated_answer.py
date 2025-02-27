def return_nth_smallest_ascii(characters):
    sorted_chars = sorted(characters[12:88], key=ord)
    return sorted_chars[16]