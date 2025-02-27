def composite_nums_between_indices(nums):
    return set((num for num in nums if num > 9 and num < 101 and (not is_prime(num))))

def is_prime(num):
    return num > 1 and all((num % i != 0 for i in range(2, num)))