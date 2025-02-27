def composite_nums_between_indices(nums):
    composite_nums = set()
    for i, num in enumerate(nums):
        if 0 <= i <= 9 and (not is_prime(num)):
            composite_nums.add(num)
    return composite_nums

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True