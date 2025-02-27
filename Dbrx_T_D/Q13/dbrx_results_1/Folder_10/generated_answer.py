def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 60:
        return None
    sorted_numbers = sorted(numbers[25:60])
    second_largest_num = None
    for i in range(len(sorted_numbers) - 1, 0, -1):
        if sorted_numbers[i] < sorted_numbers[i - 1]:
            second_largest_num = sorted_numbers[i - 1]
            break
    return second_largest_num