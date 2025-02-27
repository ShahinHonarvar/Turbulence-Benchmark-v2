def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 8:
        return None
    sorted_nums = sorted(nums[:8])
    second_smallest = None
    for num in sorted_nums:
        if sorted_nums.count(num) == 1:
            if second_smallest is None:
                second_smallest = num
            elif num > second_smallest:
                return num
    return None