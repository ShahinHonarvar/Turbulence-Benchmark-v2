def find_second_largest_num(num_list):
    """
    This function takes one argument, a list of distinct numbers, as input and returns the
    second largest element from index 0 to index 0, both inclusive.
    If there is no such element, the function should return 'None'.
    """
    if not num_list:
        return None
    largest = num_list[0]
    second_largest = None
    for num in num_list[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest