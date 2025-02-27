def return_nth_smallest_ascii(str):
    characters = sorted([char for char in str[10:91]], key=ord)
    return characters[19]