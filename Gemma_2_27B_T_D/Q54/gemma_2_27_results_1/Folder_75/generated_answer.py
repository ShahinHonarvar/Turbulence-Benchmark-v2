def all_right_truncatable_prime(nums):
    x = nums[41]
    primes = []
    for i in range(2, x):
        is_prime = True
        s = str(i)
        for j in range(len(s)):
            if int(s[j:]) not in [2, 3, 5, 7]:
                is_prime = False
                break
            if int(s[j:]) > 1:
                for k in range(2, int(int(s[j:]) ** 0.5) + 1):
                    if int(s[j:]) % k == 0:
                        is_prime = False
                        break
        if is_prime:
            primes.append(i)
    return sorted(primes)