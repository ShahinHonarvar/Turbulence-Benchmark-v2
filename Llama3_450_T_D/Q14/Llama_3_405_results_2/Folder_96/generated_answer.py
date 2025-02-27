def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    else:
        sorted_nums = sorted(numbers[50:201])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
        else:
            return None