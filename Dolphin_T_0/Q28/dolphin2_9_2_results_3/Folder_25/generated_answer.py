def return_nth_smallest_ascii(text):
    chars = [text[i] for i in range(34, 69)]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[5]