def all_right_truncatable_prime(nums):
    x = nums[126]
    primes = []
    for num in range(x, 1, -1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            temp = num
            while temp > 0:
                if temp == 1 or temp % 2 == 0:
                    prime = False
                    break
                temp //= 10
            if prime:
                primes.append(num)
    return sorted(primes, reverse=True)