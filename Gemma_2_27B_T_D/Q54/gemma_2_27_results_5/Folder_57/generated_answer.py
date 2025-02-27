def all_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for num in range(x, 1, -1):
        str_num = str(num)
        is_prime = True
        for i in range(len(str_num)):
            if not is_prime:
                break
            sub_num = int(str_num[i:])
            for j in range(2, int(sub_num ** 0.5) + 1):
                if sub_num % j == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)