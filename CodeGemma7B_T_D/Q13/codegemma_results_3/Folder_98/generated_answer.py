def find_second_largest_num(num_list):
    """Function to find the second largest number in a list of distinct numbers."""
    if len(num_list) < 2:
        return None
    num_list.sort(reverse=True)
    return num_list[1] if num_list[1] < num_list[6] else None