def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[27:56]:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0) or (num % 11 == 0) or (num % 13 == 0) or (num % 17 == 0) or (num % 19 == 0) or (num % 23 == 0) or (num % 29 == 0) or (num % 31 == 0) or (num % 37 == 0) or (num % 41 == 0) or (num % 43 == 0) or (num % 47 == 0) or (num % 53 == 0) or (num % 59 == 0) or (num % 61 == 0) or (num % 67 == 0) or (num % 71 == 0):
            composites.add(num)
    return composites