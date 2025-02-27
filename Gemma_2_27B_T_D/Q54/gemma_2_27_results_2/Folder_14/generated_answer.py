def all_right_truncatable_prime(nums):
    x = nums[78]
    primes = []
    for num in range(x, 0, -1):
        str_num = str(num)
        is_prime = True
        for i in range(len(str_num)):
            if not is_prime:
                break
            trunc_num = int(str_num[:len(str_num) - i])
            if trunc_num < 2:
                is_prime = False
            elif trunc_num % 2 == 0:
                is_prime = False
            for j in range(3, int(trunc_num ** 0.5) + 1, 2):
                if trunc_num % j == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)