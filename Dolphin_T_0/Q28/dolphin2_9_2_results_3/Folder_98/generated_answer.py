def return_nth_smallest_ascii(input_string):
    subset = input_string[0:9]
    sorted_chars = sorted(list(set(subset)), key=lambda c: ord(c))
    if len(sorted_chars) < 9:
        return None
    else:
        return sorted_chars[8]