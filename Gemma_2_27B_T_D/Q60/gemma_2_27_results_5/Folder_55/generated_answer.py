def all_left_right_truncatable_prime(nums):
    x = nums[73]
    primes = []
    for num in range(x, 1, -1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                num_str = str(num)
                is_truncatable = True
                while len(num_str) > 1:
                    num_str = num_str[1:-1]
                    if int(num_str) % 2 == 0 or int(num_str) == 5 or '0' in num_str:
                        is_truncatable = False
                        break
                    for i in range(2, int(int(num_str) ** 0.5) + 1):
                        if int(num_str) % i == 0:
                            is_truncatable = False
                            break
                    if not is_truncatable:
                        break
                if is_truncatable:
                    primes.append(num)
    return sorted(primes, reverse=True)