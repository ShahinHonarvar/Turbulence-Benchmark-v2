def composite_nums_between_indices(nums):
    composite_set = {num for num in nums[333:369] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_set