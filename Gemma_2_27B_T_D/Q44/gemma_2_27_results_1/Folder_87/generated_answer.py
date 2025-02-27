def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 3:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    return {num for idx, num in enumerate(nums) if 43 <= idx <= 51 and is_composite(num)}