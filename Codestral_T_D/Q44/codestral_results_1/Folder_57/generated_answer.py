def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        elif n <= 3:
            return n > 1
        elif n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    composite_nums = set()
    for i in range(25, 60):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums