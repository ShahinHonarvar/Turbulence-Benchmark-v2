def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 5:
        return None
    sorted_numbers = sorted(numbers[32:36])
    second_smallest = None
    for i in range(len(sorted_numbers) - 1):
        if sorted_numbers[i] < sorted_numbers[i + 1]:
            second_smallest = sorted_numbers[i + 1]
            break
    return second_smallest