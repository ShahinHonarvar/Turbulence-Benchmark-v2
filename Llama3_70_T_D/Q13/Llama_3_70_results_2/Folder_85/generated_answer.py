def find_second_largest_num(nums):
    try:
        second_largest = sorted(nums[6:9])[-2]
        return second_largest
    except IndexError:
        return None