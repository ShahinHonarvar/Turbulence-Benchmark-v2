def composite_nums_between_indices(nums):
    composites = {x for x in nums[31:73] if not is_prime(x)}
    return composites