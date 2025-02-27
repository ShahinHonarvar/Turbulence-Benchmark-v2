def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def composite_nums_between_indices(nums):
    return set((num for num in nums[15:40] if not is_prime(num)))