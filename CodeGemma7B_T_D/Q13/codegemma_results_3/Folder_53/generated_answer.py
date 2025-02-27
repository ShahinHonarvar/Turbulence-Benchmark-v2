def find_second_largest_num(nums):
    items = nums[100:201]
    if not items:
        return None
    items.sort(reverse=True)
    return items[1]