def all_left_truncatable_prime(nums):
    x = nums[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x, 1, -1):
        str_i = str(i)
        if '0' not in str_i and all((is_prime(int(str_i[j:])) for j in range(len(str_i)))):
            primes.append(i)
    return sorted(primes, reverse=True)