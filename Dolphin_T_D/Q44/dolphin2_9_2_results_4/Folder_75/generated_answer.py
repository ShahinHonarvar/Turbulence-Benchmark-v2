def composite_nums_between_indices(nums):

    def is_composite(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                return True
        return False
    return {nums[i] for i in range(75, 86) if is_composite(nums[i])}