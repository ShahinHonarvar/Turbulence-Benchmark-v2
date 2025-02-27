def find_second_largest_num(num_list):
    """Returns the second largest element from index 0 to 6, both inclusive. Returns 'None' if there is no such element."""
    num_list.sort(reverse=True)
    if len(num_list) < 2 or num_list[0] == num_list[1]:
        return None
    return num_list[1]