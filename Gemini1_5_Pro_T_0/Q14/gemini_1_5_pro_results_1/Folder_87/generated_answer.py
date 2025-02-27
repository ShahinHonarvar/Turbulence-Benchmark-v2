def find_second_smallest_num(numbers):
    if len(numbers) < 89 or len(numbers[:22]) + len(numbers[22:89]) < 2:
        return None
    else:
        sorted_nums = sorted(numbers[22:89])
        return sorted_nums[1]