def all_right_truncatable_prime(nums):
    x = nums[97]
    primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(2, x):
        if is_prime(i):
            flag = True
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    flag = False
                    break
                temp //= 10
            if flag:
                primes.append(i)
    return sorted(primes)