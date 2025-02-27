def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    largest = second_largest = float('-inf')
    for num in numbers[:8]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest