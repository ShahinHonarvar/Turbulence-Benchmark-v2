def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num_1, min_num_2 = (max(numbers), min(numbers))
    for num in numbers[1:6]:
        if min_num_1 == num:
            continue
        if num < min_num_1 and num > min_num_2:
            min_num_1, min_num_2 = (num, min_num_1)
        elif num < min_num_2:
            min_num_2 = num
    if min_num_2 == min_num_1:
        return None
    return min_num_2