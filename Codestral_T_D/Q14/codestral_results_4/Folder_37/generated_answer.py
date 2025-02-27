def find_second_smallest_num(numbers):
    if 5 <= len(numbers) <= 7:
        sorted_nums = sorted(numbers[5:])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None