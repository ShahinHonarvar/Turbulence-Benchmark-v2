def return_nth_smallest_ascii(letters):
    sorted_letters = sorted(letters[5:83], key=ord)
    return sorted_letters[15]