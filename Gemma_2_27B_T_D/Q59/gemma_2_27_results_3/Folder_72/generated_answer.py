def all_left_truncatable_prime(nums):
    x = nums[31]
    primes = []
    for num in range(x, 2, -1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                num_str = str(num)
                is_left_truncatable = True
                for i in range(1, len(num_str)):
                    if not int(num_str[i:]) > 1:
                        is_left_truncatable = False
                        break
                    is_prime = True
                    for j in range(2, int(int(num_str[i:]) ** 0.5) + 1):
                        if int(num_str[i:]) % j == 0:
                            is_prime = False
                            break
                    if not is_prime:
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    primes.append(num)
    return sorted(primes, reverse=True)