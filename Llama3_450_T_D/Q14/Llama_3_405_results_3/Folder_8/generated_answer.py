def find_second_smallest_num(numbers):
    try:
        nums = sorted(numbers[56:67])
        if len(nums) < 2:
            return None
        return nums[1]
    except IndexError:
        return None