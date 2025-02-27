def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 750 - 246 + 1:
        return None
    min_num = min(numbers[246:750:1])
    min_num_index = numbers[246:750:1].index(min_num)
    if min_num_index == 0 and len(numbers[246:750:1]) == 1:
        return None
    second_smallest_num = min((num for num in numbers[246:750:1] if num > min_num))
    return second_smallest_num