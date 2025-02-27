def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('-inf')
    first_largest = min_num
    second_largest = min_num
    for i in range(35, 50):
        if not isinstance(numbers[i], (int, float)):
            raise ValueError('All elements in the list must be numbers.')
        if numbers[i] > first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < first_largest:
            second_largest = numbers[i]
    if second_largest == min_num:
        return None
    return second_largest