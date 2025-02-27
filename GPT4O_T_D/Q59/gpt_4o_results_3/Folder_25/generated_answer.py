def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable(prime):
        str_prime = str(prime)
        while len(str_prime) > 0:
            if not is_prime(int(str_prime)):
                return False
            str_prime = str_prime[1:]
        return True
    x = nums[92]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)