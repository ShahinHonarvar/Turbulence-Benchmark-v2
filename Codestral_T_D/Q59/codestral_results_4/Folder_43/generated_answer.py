def all_left_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for num in range(x, 1, -1):
        if str(num).count('0') == 0:
            is_truncatable = True
            for i in range(1, len(str(num))):
                if int(str(num)[i:]) not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    primes.sort(reverse=True)
    return primes