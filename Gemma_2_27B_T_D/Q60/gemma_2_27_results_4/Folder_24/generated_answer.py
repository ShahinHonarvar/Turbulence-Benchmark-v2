def all_left_right_truncatable_prime(nums):
    x = nums[65]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[:j]) in [2, 3, 5, 7] and int(str(i)[j:]) in [2, 3, 5, 7] for j in range(1, len(str(i))))):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    primes.sort(reverse=True)
    return primes