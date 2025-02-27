def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    smallest, second_smallest = (nums[0], nums[1])
    if smallest > second_smallest:
        smallest, second_smallest = (second_smallest, smallest)
    for num in nums[1:]:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if len(nums) > 1 else None