def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    second_largest = float('-inf')
    for num in numbers[43:52]:
        if num > second_largest:
            if second_largest == min_num:
                min_num = second_largest
            second_largest = num
        elif num > min_num and num < second_largest:
            min_num = num
    if second_largest == float('-inf'):
        return None
    return second_largest