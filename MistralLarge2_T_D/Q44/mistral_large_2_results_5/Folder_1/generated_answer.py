def composite_nums_between_indices(nums):
    if not nums:
        return set()

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for idx, num in enumerate(nums) if 69 <= idx <= 83 and is_composite(num)}