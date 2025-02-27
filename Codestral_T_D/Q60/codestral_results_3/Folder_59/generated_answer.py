def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[84]
    trunc_primes = []
    for i in range(2, x + 1):
        if '0' not in str(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num = int(str(num)[1:]) if num > 10 else 0
            else:
                num = i
                while num > 0:
                    if not is_prime(num):
                        break
                    num = int(str(num)[:-1])
                else:
                    trunc_primes.append(i)
    return sorted(trunc_primes, reverse=True)