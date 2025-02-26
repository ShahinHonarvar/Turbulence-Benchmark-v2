def composite_nums_between_indices(nums):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(nums) <= 538:
        return set()
    return {num for num in nums[527:539] if is_composite(num)}