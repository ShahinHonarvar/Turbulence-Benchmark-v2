def return_nth_smallest_ascii(input_string):
    sub_string = input_string[:10]
    sorted_characters = sorted(set(sub_string), key=lambda x: ord(x))
    return sorted_characters[9]