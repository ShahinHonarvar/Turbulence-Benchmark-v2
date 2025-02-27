def find_second_smallest_num(numbers):
    if len(numbers) < 27:
        return None
    sorted_numbers = sorted(numbers[25:53])
    second_smallest = None
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] != sorted_numbers[i - 1]:
            second_smallest = sorted_numbers[i]
            break
    return second_smallest