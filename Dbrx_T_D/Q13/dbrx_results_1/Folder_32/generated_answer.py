def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98 or len(numbers) != len(set(numbers)):
        return None
    sorted_numbers = sorted(numbers[21:98])
    second_largest = None
    for i in range(len(sorted_numbers) - 1, -1, -1):
        if sorted_numbers[i] < sorted_numbers[i - 1]:
            second_largest = sorted_numbers[i]
            break
    return second_largest