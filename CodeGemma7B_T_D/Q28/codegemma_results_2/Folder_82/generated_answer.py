def return_nth_smallest_ascii(text):
    return min(text[0:15], key=ord)