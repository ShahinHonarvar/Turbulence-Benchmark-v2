def all_left_truncatable_prime(n):
    nums = set(n)
    primes = {2, 3, 5, 7}

    def is_prime(n):
        if n in primes or n <= 1:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    result = []
    for num in nums:
        if is_left_truncatable(num):
            result.append(num)
    return sorted(result)