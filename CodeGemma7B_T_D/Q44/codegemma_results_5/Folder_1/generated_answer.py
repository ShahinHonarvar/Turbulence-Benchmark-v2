def composite_nums_between_indices(nums):
    result = set()
    for num in nums[69:84]:
        if num != 1 and (not is_prime(num)):
            result.add(num)
    return result

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True