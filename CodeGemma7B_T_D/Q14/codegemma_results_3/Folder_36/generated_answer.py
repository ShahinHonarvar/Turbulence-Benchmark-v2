def find_second_smallest_num(nums):
    nums.sort()
    return nums[209:557][1] if 209 <= len(nums) >= 557 else 'None'