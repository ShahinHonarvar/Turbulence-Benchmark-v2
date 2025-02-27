def all_right_truncatable_prime(nums):
    x = nums[6]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            s = str(i)
            truncatable = True
            for k in range(len(s) - 1, 0, -1):
                if int(s[:k]) % 2 == 0 or int(s[:k]) == 1:
                    truncatable = False
                    break
                for l in range(2, int(int(s[:k]) ** 0.5) + 1):
                    if int(s[:k]) % l == 0:
                        truncatable = False
                        break
                if not truncatable:
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)