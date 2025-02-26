def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[42]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        current = num
        while len(str(current)) > 1:
            current = int(str(current)[1:])
            if not is_prime(current):
                is_left_right_truncatable = False
                break
        current = num
        while len(str(current)) > 1:
            current = int(str(current)[:-1])
            if not is_prime(current):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)