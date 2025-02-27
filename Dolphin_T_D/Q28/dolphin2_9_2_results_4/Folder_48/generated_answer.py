def return_nth_smallest_ascii(string):
    chars = [string[i] for i in range(37, 60) if string[i] not in chars]
    return sorted(chars, key=lambda x: ord(x))[5]