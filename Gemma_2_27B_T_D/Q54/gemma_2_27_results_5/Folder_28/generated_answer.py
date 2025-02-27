def all_right_truncatable_prime(nums):
    x = nums[19]
    primes = []
    for i in range(2, x):
        is_prime = True
        num_str = str(i)
        for j in range(len(num_str)):
            if int(num_str[:len(num_str) - j]) % 2 == 0 and int(num_str[:len(num_str) - j]) != 2:
                is_prime = False
                break
            for k in range(3, int(int(num_str[:len(num_str) - j]) ** 0.5) + 1, 2):
                if int(num_str[:len(num_str) - j]) % k == 0:
                    is_prime = False
                    break
            if not is_prime:
                break
        if is_prime:
            primes.append(i)
    return sorted(primes)