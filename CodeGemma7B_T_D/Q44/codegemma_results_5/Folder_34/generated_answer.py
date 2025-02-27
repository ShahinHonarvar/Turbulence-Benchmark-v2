def composite_nums_between_indices(nums):
    composite_nums = []
    for i in range(70, 201):
        if i in nums and (not is_prime(i)):
            composite_nums.append(i)
    return set(composite_nums)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True