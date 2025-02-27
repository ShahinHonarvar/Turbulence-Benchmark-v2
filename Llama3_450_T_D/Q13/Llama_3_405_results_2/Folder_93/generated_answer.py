def find_second_largest_num(numbers):
    try:
        nums = sorted(numbers[75:95])
        if len(nums) >= 2:
            return nums[-2]
    except IndexError:
        pass