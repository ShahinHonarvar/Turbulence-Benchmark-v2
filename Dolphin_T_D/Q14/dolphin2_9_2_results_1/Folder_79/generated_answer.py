def find_second_smallest_num(nums):
    indices = range(1, 6)
    if not all((nums[i] != nums[i + 1] for i in indices[:-1])):
        return None
    else:
        return sorted((nums[i] for i in indices))[1]