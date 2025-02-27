def all_left_truncatable_prime(nums):
    x = nums[41]
    primes = []
    for num in range(2, x):
        is_prime = True
        num_str = str(num)
        if '0' in num_str:
            continue
        for i in range(len(num_str)):
            if not is_prime:
                break
            trunc_num = int(num_str[i:])
            for j in range(2, int(trunc_num ** 0.5) + 1):
                if trunc_num % j == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    return sorted(primes)