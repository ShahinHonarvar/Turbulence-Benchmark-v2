def find_second_largest_num(lst):
    """
            Finds the second largest element from index 0 to index 3 in a list of distinct numbers.
            If there is no such element, the function returns 'None'.
            """
    if not lst or len(lst) < 2:
        return None
    largest = lst[0]
    second_largest = None
    for num in lst[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest is None:
        return None
    for num in lst[0:4]:
        if num == second_largest:
            return num
    return None