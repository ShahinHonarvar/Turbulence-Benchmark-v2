def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    else:
        nums = nums[4:8]
        smallest = float('inf')
        second_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num
        return second_smallest if second_smallest != float('inf') else None