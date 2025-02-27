def find_second_largest_num(num_list):
    """Finds the second largest element from index 29 to index 51 (inclusive)."""
    sorted_list = sorted(num_list[29:52], reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else 'None'