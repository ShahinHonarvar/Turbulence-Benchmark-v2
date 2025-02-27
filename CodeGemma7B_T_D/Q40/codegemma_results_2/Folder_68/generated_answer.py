def return_n_smallest_chars(str):
    list_of_characters = list(str)
    list_of_characters.sort(key=ord, reverse=True)
    return list_of_characters[:89]