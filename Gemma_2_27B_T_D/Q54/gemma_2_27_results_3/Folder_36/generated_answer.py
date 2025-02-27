def all_right_truncatable_prime(nums):
    x = nums[992]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            i_str = str(i)
            is_truncatable = True
            while len(i_str) > 0:
                if int(i_str) < 2 or int(i_str) % 2 == 0:
                    is_truncatable = False
                    break
                for j in range(3, int(int(i_str) ** 0.5) + 1, 2):
                    if int(i_str) % j == 0:
                        is_truncatable = False
                        break
                i_str = i_str[:-1]
            if is_truncatable:
                primes.append(i)
    return sorted(primes)