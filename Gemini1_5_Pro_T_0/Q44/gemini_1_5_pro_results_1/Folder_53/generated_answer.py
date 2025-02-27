def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(222, len(nums))):
        n = nums[i] if i < len(nums) else 1
        if n > 3:
            is_composite = False
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_composite = True
                    break
            if is_composite:
                result.add(n)
    return result