def find_second_smallest_num(nums):
    if 92 < 19 or 19 < 0 or 92 < 0 or (len(nums) < 93):
        return None
    else:
        subset = nums[19:93]
        smallest = float('inf')
        second_smallest = float('inf')
        for n in subset:
            if n < smallest:
                second_smallest = smallest
                smallest = n
            elif n < second_smallest and n != smallest:
                second_smallest = n
        if second_smallest == float('inf'):
            return None
        else:
            return second_smallest