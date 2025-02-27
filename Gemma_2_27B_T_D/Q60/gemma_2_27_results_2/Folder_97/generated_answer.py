def all_left_right_truncatable_prime(nums):
    x = nums[645]
    primes = []
    for num in range(2, x + 1):
        if num in [2, 3, 5, 7]:
            primes.append(num)
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            continue
        else:
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
                    if int(num_str) == 0 or int(num_str) % 2 == 0 or int(num_str) % 3 == 0 or (int(num_str) % 5 == 0) or (int(num_str) % 7 == 0):
                        is_truncatable = False
                        break
                    for i in range(2, int(int(num_str) ** 0.5) + 1):
                        if int(num_str) % i == 0:
                            is_truncatable = False
                            break
                    if not is_truncatable:
                        break
                    par
                if is_truncatable:
                    primes.append(num)
    return sorted(primes)