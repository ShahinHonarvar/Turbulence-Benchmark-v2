def return_nth_smallest_ascii(characters):
    return min(characters[0:15], key=ord)