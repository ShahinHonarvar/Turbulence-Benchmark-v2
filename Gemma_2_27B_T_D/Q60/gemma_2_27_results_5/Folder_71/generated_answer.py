def all_left_right_truncatable_prime(nums):
    x = nums[22]
    primes = []
    for num in range(2, x + 1):
        if num <= 9:
            if num > 1:
                primes.append(num)
        else:
            str_num = str(num)
            if '0' not in str_num:
                is_prime = True
                temp = str_num
                while len(temp) > 1:
                    if not (int(temp) > 1 and all((int(temp) % i for i in range(2, int(temp ** 0.5) + 1)))):
                        is_prime = False
                        break
                    temp = temp[1:]
                temp = str_num
                while len(temp) > 1:
                    if not (int(temp) > 1 and all((int(temp) % i for i in range(2, int(temp ** 0.5) + 1)))):
                        is_prime = False
                        break
                    temp = temp[:-1]
                if is_prime:
                    primes.append(num)
    return sorted(primes, reverse=True)