def composite_nums_between_indices(nums):
    composite_numbers = set()
    for num in nums[5:]:
        if not is_prime(num):
            composite_numbers.add(num)
    return composite_numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True