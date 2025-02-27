def all_right_truncatable_prime(nums):
    candidate = nums[29]
    truncatable_primes = []
    for i in range(candidate):
        num = i
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            str_num = str(num)
            for digit in str_num[:-1]:
                num = int(str_num)
                str_num, digit = (str_num[:-1], str_num[-1])
                num = int(str_num)
                is_prime = True
                for divisor in range(2, int(num ** 0.5) + 1):
                    if num % divisor == 0:
                        is_prime = False
                        break
                if not is_prime:
                    break
            if is_prime:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)