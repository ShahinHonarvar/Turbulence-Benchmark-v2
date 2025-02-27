def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(nums) < 43:
        return set()
    result = set()
    for num in nums[42:69]:
        if is_composite(num):
            result.add(num)
    return result