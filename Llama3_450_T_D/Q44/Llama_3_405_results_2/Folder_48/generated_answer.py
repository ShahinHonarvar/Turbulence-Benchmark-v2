import math

def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(nums) if 661 <= i <= 924 and is_composite(num)))