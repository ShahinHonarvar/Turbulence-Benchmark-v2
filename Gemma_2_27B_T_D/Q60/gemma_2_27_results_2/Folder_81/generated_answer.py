def all_left_right_truncatable_prime(nums):
    x = nums[98]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' in s:
            continue
        is_prime = True
        while len(s) > 1:
            if not (int(s) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] or (int(s) % 2 != 0 and int(s) % 3 != 0)):
                is_prime = False
                break
            s = s[1:-1]
        if is_prime:
            primes.append(i)
    return sorted(primes)