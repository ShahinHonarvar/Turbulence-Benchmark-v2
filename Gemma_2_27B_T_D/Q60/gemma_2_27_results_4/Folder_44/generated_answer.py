def all_left_right_truncatable_prime(nums):
    x = nums[39]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if '0' not in str(i):
            is_truncatable = True
            temp = str(i)
            while len(temp) > 1:
                if not is_prime(int(temp)) or not is_prime(int(temp[1:])):
                    is_truncatable = False
                    break
                temp = temp[1:-1]
            if is_truncatable:
                primes.append(i)
    return sorted(primes)