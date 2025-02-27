def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[803]
    truncatable_primes = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        is_truncatable_prime = True
        num_str = str(i)
        for j in range(1, len(num_str)):
            if not is_prime(int(num_str[j:])) or not is_prime(int(num_str[:-j])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return truncatable_primes