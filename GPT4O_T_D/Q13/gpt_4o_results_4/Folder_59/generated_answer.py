def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    limited_list = numbers[:10]
    largest = second_largest = float('-inf')
    for num in limited_list:
        if num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest