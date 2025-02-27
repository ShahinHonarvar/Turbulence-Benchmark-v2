def find_second_largest_num(numbers):
    if len(numbers) < 89 or 22 > len(numbers):
        return None
    sliced_list = numbers[22:89]
    if len(set(sliced_list)) < 2:
        return None
    largest = max(sliced_list)
    sliced_list.remove(largest)
    return max(sliced_list)