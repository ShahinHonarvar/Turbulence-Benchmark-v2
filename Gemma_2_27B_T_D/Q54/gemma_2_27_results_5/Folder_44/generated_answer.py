def all_right_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            temp = num
            while temp > 0:
                if temp % 2 == 0 or temp < 2:
                    break
                is_truncatable = True
                for i in range(2, int(temp ** 0.5) + 1):
                    if temp % i == 0:
                        is_truncatable = False
                        break
                if not is_truncatable:
                    break
                temp //= 10
            if temp == 0:
                primes.append(num)
    return sorted(primes)