def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    largest = second_largest = float('-inf')
    for num in numbers[:6]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest