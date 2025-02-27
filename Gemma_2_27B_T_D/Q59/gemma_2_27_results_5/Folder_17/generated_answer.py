def all_left_truncatable_prime(nums):
    x = nums[36]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(x, 1, -1):
        string = str(num)
        if '0' not in string:
            is_left_truncatable = True
            for i in range(len(string)):
                if not is_prime(int(string[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)