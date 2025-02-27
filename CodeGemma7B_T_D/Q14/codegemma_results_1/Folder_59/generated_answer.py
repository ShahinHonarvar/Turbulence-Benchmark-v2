def find_second_smallest_num(numbers):
    """
    This function takes one argument, a list of distinct numbers,
    as input and returns the second smallest element from index 0 to index 9,
    both inclusive. If there is no such an element, the function should return
    'None'.
    """
    if len(numbers) < 2:
        return 'None'
    min_num = float('inf')
    second_min_num = float('inf')
    for num in numbers:
        if num < min_num:
            min_num, second_min_num = (num, min_num)
        elif num < second_min_num and num != min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return 'None'
    return second_min_num