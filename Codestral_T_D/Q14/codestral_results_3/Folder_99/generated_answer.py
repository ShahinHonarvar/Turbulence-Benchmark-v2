def find_second_smallest_num(numbers):
    if 608 <= len(numbers) <= 609:
        sorted_nums = sorted(numbers[608:609])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None