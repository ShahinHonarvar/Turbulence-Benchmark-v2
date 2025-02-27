def composite_nums_between_indices(nums):
    if len(nums) < 21:
        return set()
    return {num for num in nums[20:31] if num > 1 and (not (num == 2 or (num % 2 != 0 and num > 3 and any((num % i == 0 for i in range(3, int(num ** 0.5) + 1))))))}