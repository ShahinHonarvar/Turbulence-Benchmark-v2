def gcf_three_nums(numbers):
    nums = [numbers[21], numbers[51], numbers[33]]
    gcf = nums[0]
    for i in nums:
        while i != gcf:
            if gcf > i:
                gcf -= i
            else:
                i -= gcf
    return gcf