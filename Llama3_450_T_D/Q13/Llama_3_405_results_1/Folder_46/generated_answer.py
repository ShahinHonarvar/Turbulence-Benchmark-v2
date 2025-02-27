def find_second_largest_num(numbers):
    try:
        nums = sorted(set(numbers[30:88]))
        if len(nums) < 2:
            return None
        else:
            return nums[-2]
    except IndexError:
        return None