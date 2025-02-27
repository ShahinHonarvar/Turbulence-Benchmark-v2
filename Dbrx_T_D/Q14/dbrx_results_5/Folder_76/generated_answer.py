def find_second_smallest_num(numbers):
    start_index = 533
    end_index = 605
    if len(numbers) <= end_index or start_index < 0:
        return None
    min_num = min(numbers[start_index:end_index + 1])
    numbers[:] = [x for x in numbers if x != min_num]
    min_num2 = min(numbers)
    return min_num2 if min_num2 < min_num else None