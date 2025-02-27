def all_right_truncatable_prime(nums):
    x = nums[55]
    primes = []
    for i in range(2, x):
        prime = True
        s = str(i)
        for j in range(len(s)):
            if int(s[j:]) not in [2, 3, 5, 7] and int(s[j:]) % 2 == 0 or int(s[j:]) % 3 == 0 or (int(s[j:]) > 1 and all((int(s[j:]) % k for k in range(5, int(int(s[j:]) ** 0.5) + 1, 6))) != 0):
                prime = False
                break
        if prime:
            primes.append(i)
    return sorted(primes)