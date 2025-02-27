def all_left_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            i_str = str(i)
            left_truncatable = True
            for k in range(1, len(i_str)):
                if int(i_str[k:]) not in primes or '0' in i_str[k:]:
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(i)
    return sorted(primes)