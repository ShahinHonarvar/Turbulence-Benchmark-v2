def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    second_smallest_num = min(numbers[75:95])
    nums_set = set(numbers[75:95])
    nums_set.remove(second_smallest_num)
    if len(nums_set) == 0:
        return None
    return min(nums_set)