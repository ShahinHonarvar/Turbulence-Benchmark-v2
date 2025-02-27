def all_left_right_truncatable_prime(nums):
    x = nums[767]
    primes = []
    for num in range(x, 1, -1):
        if not '0' in str(num):
            is_prime = True
            n = num
            while n > 9:
                if not is_prime:
                    break
                n_str = str(n)
                n //= 10
                if not is_prime_number(n):
                    is_prime = False
                n = int(n_str[1:])
                if not is_prime_number(n):
                    is_prime = False
            if is_prime and is_prime_number(num):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True