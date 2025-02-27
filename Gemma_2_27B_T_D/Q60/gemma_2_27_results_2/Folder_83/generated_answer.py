def all_left_right_truncatable_prime(nums):
    x = nums[24]
    primes = []
    for num in range(2, x + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                num_str = str(num)
                truncatable = True
                while len(num_str) > 1:
                    if int(num_str) not in [2, 3, 5, 7] and int(num_str) % 2 == 0 or int(num_str) % 3 == 0 or int(num_str) % 5 == 0 or (int(num_str) % 7 == 0):
                        truncatable = False
                        break
                    num_str = num_str[1:-1]
                if truncatable:
                    primes.append(num)
    return sorted(primes)