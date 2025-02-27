def all_left_truncatable_prime(nums):
    x = nums[4]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if not '0' in str(i):
            isPrime = True
            temp = str(i)
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    isPrime = False
                    break
                temp = temp[1:]
            if isPrime:
                primes.append(i)
    return sorted(primes)