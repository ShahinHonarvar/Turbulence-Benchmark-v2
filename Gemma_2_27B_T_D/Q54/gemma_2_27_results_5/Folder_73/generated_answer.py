def all_right_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for num in range(2, x):
        is_prime = True
        str_num = str(num)
        for i in range(len(str_num)):
            if int(str_num[i:]) not in [2, 3, 5, 7]:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)