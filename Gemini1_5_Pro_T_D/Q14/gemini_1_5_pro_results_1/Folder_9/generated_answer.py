def find_second_smallest_num(numbers):
    if len(numbers) < 201 or min(numbers[70:201]) == max(numbers[70:201]):
        return None
    else:
        sorted_nums = sorted(numbers[70:201])
        return sorted_nums[1]