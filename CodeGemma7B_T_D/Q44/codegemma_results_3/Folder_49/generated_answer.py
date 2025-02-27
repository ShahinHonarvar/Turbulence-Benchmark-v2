def composite_nums_between_indices(nums):
    comp_nums = set((num for num in nums if all((elem % num == 0 for elem in range(2, num)))))
    return {num for num in comp_nums if nums.index(num) >= 90 and nums.index(num) <= 200}