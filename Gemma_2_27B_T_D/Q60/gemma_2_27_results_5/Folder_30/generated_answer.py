def all_left_right_truncatable_prime(nums):
    x = nums[37]
    primes = []
    for num in range(2, x + 1):
        if all((2 ** (num - 1) % i != 1 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            flag = True
            n = num
            while n > 9:
                n //= 10
                if not all((2 ** (n - 1) % i != 1 for i in range(2, int(n ** 0.5) + 1))):
                    flag = False
                    break
            n = num
            while n > 9:
                n %= 10 ** (len(str(n)) - 1)
                if not all((2 ** (n - 1) % i != 1 for i in range(2, int(n ** 0.5) + 1))):
                    flag = False
                    break
            if flag:
                primes.append(num)
    primes.sort(reverse=True)
    return primes