def return_nth_smallest_ascii(str):
    return sorted([i for i in str[3:27] if ord(i) >= ord('Z')])[4]