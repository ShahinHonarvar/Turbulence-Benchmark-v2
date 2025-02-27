def all_left_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' not in str_i:
            is_prime = True
            for j in range(1, len(str_i)):
                if not (int(str_i[j:]) in [2, 3, 5, 7] or int(str_i[:j]) in [2, 3, 5, 7]) or not (int(str_i[j:]) > 1 and int(str_i[:j]) > 1):
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)