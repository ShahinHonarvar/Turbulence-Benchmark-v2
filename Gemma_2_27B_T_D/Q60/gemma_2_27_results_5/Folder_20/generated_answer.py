def all_left_right_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[:j]) and int(str(i)[:-j]) for j in range(1, len(str(i))))) and all((str(j) != '0' for j in str(i))):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)