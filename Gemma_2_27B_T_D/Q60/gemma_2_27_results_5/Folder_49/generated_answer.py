def all_left_right_truncatable_prime(nums):
    x = nums[14]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_prime = True
            n = num
            while n > 9:
                if n % 2 == 0 or any((n % i == 0 for i in range(3, int(n ** 0.5) + 1, 2))):
                    is_prime = False
                    break
                n = int(str(n)[1:])
            n = num
            while n > 9:
                if n % 2 == 0 or any((n % i == 0 for i in range(3, int(n ** 0.5) + 1, 2))):
                    is_prime = False
                    break
                n = int(str(n)[:-1])
            if is_prime:
                primes.append(num)
    return sorted(primes)