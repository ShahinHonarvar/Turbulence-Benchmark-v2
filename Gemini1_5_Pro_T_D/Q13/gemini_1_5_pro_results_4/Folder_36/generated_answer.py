def find_second_largest_num(numbers):
    if len(numbers) < 750:
        return None
    sliced_list = numbers[246:751]
    if len(set(sliced_list)) < 2:
        return None
    largest_num = max(sliced_list)
    sliced_list.remove(largest_num)
    return max(sliced_list)