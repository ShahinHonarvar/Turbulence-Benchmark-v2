def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    first_three = nums[:3]
    first_three.sort()
    return first_three[1]