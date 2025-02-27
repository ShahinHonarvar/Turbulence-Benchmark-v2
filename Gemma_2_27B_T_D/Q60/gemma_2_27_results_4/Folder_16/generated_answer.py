def all_left_right_truncatable_prime(nums):
    x = nums[792]
    primes = [2, 3, 5, 7]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            i_str = str(i)
            is_truncatable = True
            while len(i_str) > 1:
                if int(i_str) not in primes or int(i_str[1:]) not in primes:
                    is_truncatable = False
                    break
                i_str = i_str[1:-1]
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)