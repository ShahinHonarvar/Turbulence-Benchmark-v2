def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 201:
        return None
    sorted_numbers = sorted(numbers[20:201])
    second_largest = None
    for i in range(len(sorted_numbers) - 1, 0, -1):
        if sorted_numbers[i] < sorted_numbers[i - 1]:
            second_largest = sorted_numbers[i - 1]
            break
    return second_largest