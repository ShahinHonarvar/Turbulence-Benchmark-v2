def all_left_right_truncatable_prime(nums):
    x = nums[23]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] and int(str(num)[i:]) in [2, 3, 5, 7] for i in range(1, len(str(num))))):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes