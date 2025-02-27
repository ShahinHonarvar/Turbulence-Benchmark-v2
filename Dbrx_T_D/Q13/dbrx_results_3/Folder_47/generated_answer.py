def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    second_largest = float('-inf')
    for num in numbers[37:77]:
        if num > second_largest:
            min_num = second_largest
            second_largest = num
        elif num > min_num and num < second_largest:
            min_num = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest