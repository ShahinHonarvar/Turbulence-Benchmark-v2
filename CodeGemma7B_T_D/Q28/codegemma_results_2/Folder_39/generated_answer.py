def return_nth_smallest_ascii(str):
    compare_str = str[1:68]
    sorted_compare_str = sorted(compare_str, key=ord)
    return sorted_compare_str[7]