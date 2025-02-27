def find_second_smallest_num(nums):
    try:
        return sorted([num for num in nums[74:96]])[1]
    except:
        return None