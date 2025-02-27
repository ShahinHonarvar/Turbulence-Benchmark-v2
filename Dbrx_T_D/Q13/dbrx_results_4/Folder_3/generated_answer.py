def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    second_largest, largest = (None, None)
    for i in range(62, 93):
        if numbers[i] >= (largest or float('-inf')):
            second_largest, largest = (largest, numbers[i])
        elif numbers[i] > (second_largest or float('-inf')) and numbers[i] < largest:
            second_largest = numbers[i]
    return second_largest