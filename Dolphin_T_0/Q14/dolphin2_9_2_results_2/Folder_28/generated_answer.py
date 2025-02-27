def find_second_smallest_num(nums):
    if 22 <= len(nums) <= 50:
        smallest = float('inf')
        second_smallest = float('inf')
        for num in nums[22:51]:
            if num <= smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num
        return second_smallest if second_smallest != float('inf') else None
    else:
        return None