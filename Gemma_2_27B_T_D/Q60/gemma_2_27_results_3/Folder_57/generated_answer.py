def all_left_right_truncatable_prime(nums):
    x = nums[54]
    primes = [2, 3, 5, 7]
    for i in range(2, x + 1):
        if all((i % j for j in primes)):
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        if p < 10:
            truncatable_primes.append(p)
        else:
            p_str = str(p)
            valid = True
            while len(p_str) > 1:
                if int(p_str) not in primes or int(p_str[1:]) not in primes:
                    valid = False
                    break
                p_str = p_str[1:]
            if valid:
                truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)