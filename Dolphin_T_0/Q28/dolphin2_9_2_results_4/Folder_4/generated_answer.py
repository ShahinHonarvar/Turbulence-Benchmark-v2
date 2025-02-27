def return_nth_smallest_ascii(string):
    restricted_string = string[9:23]
    sorted_string = sorted(restricted_string, key=lambda x: ord(x))
    return sorted_string[3]