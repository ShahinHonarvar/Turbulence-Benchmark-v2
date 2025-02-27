def return_nth_smallest_ascii(str):
    list_of_ascii_vals = []
    for char in str:
        list_of_ascii_vals.append(ord(char))
    list_of_ascii_vals.sort()
    return chr(list_of_ascii_vals[3])