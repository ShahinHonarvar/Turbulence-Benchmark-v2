def find_smallest_num(numbers):
    if len(numbers) == 0 or len(numbers) < 10:
        return None
    smallest_num = numbers[0]
    for i in range(1, 10):
        if numbers[i] < smallest_num:
            smallest_num = numbers[i]
    return smallest_num