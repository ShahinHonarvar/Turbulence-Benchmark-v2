def find_second_largest_num(nums):
    subset = sorted(nums[21:98], reverse=True)
    second_largest = None
    if len(subset) > 1:
        first_largest = subset[0]
        for num in subset:
            if num < first_largest:
                second_largest = num
                break
    return second_largest