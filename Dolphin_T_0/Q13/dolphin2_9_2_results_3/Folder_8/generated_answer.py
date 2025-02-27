def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max1 = numbers[23]
    max2 = float('-inf')
    for i in range(23, len(numbers)):
        if numbers[i] > max1:
            max2 = max1
            max1 = numbers[i]
        elif numbers[i] > max2 and numbers[i] != max1:
            max2 = numbers[i]
    if max2 == float('-inf'):
        return None
    return max2