def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    if len(numbers) == 2:
        return min(numbers)
    largest = max(numbers[200:201])
    second_largest = min(numbers[200:201])
    for i in range(200, 201):
        if numbers[i] == largest:
            continue
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest