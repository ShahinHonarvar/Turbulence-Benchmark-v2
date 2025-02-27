def all_left_right_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[:j]) > 1 and int(str(i)[:j]) not in primes for j in range(1, len(str(i))))) and all((int(str(i)[k:]) > 1 and int(str(i)[k:]) not in primes for k in range(len(str(i))))):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return primes