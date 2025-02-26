def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[29]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            current = num
            while len(str(current)) > 1:
                current = int(str(current)[1:])
                if not is_prime(current):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)