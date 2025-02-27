def composite_nums_between_indices(nums):
    composites = set()
    for i in range(1, len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            product = nums[i - 1] * nums[j - 1]
            if product > 1 and (not is_prime(product)):
                composites.add(product)
    return composites

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True