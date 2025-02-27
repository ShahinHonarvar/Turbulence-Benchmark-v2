def all_left_right_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for num in range(2, x + 1):
        if num < 10 and all((num % i for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
        else:
            str_num = str(num)
            is_prime = True
            while len(str_num) > 1:
                if str_num[0] == '0' or not all((int(str_num) % i for i in range(2, int(int(str_num) ** 0.5) + 1))):
                    is_prime = False
                    break
                str_num = str_num[1:-1]
            if is_prime:
                primes.append(num)
    return sorted(primes, reverse=True)