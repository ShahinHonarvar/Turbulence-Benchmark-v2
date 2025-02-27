def all_right_truncatable_prime(nums):
    x = nums[36]
    prime_list = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable_prime(num):
            prime_list.append(num)
    return sorted(prime_list)

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    temp = num
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True