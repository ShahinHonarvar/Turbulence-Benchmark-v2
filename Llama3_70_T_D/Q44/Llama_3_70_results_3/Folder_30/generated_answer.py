def composite_nums_between_indices(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return {num for i, num in enumerate(nums) if 19 <= i <= 92 and (not is_prime(num))}