def find_second_largest_num(num_list):
    """
    Returns the second largest element from index 0 to index 5,
    inclusive, from a list of distinct numbers.
    """
    if not num_list or len(num_list) <= 1:
        return None
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in num_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    if second_largest < float('-inf'):
        return None
    return second_largest