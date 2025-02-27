def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers[31:35])
    if len(sorted_numbers) < 2:
        return None
    second_largest = None
    for i in range(len(sorted_numbers) - 1, -1, -1):
        if sorted_numbers[i] != max(sorted_numbers):
            second_largest = sorted_numbers[i]
            break
    return second_largest