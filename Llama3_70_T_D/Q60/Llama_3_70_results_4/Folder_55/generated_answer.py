def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    prime_set = {i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)}
    truncatable_primes = []
    for num in prime_set:
        num_str = str(num)
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(num_str)):
            if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:-i]))):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)