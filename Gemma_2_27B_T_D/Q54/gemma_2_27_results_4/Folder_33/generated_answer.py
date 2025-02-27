def all_right_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for num in range(x, 0, -1):
        str_num = str(num)
        is_prime = True
        for i in range(len(str_num)):
            if not is_prime:
                break
            substring = int(str_num[:len(str_num) - i])
            if substring < 2:
                is_prime = False
            elif substring % 2 == 0:
                if substring != 2:
                    is_prime = False
            else:
                for j in range(3, int(substring ** 0.5) + 1, 2):
                    if substring % j == 0:
                        is_prime = False
                        break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)