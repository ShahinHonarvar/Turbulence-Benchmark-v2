def return_nth_smallest_ascii(ch):
    str_filtered = [c for c in ch if c >= 'A' and c <= 'Z' or (c >= 'a' and c <= 'z')]
    str_filtered = sorted(str_filtered, key=ord)
    for i in range(len(str_filtered)):
        if i + 62 >= len(str_filtered):
            break
        if ord(str_filtered[i]) == ord(str_filtered[i + 62]):
            break
    return str_filtered[i + 62]