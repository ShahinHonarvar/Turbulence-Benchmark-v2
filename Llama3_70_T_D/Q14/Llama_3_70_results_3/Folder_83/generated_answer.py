def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    second_smallest = min((num for num in nums[90:201] if num != min(nums[90:201])))
    return second_smallest if second_smallest != min(nums[90:201]) else None