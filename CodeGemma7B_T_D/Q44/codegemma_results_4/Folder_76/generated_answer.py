def composite_nums_between_indices(nums):
    composites = set()
    for i in range(639, 976):
        if not is_prime(nums[i]):
            composites.add(nums[i])
    return composites

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True