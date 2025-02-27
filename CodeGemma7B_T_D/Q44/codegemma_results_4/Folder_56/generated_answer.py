def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[0:0 + 1]:
        if num not in [2, 3] and num % 2 != 0 and (num % 3 != 0):
            for i in range(5, num, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    composites.add(num)
    return composites