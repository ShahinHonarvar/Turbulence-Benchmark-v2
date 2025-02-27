def all_right_truncatable_prime(nums):
    x = nums[29]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            tr = str(i)
            truncatable = True
            while len(tr) > 1:
                tr = tr[:-1]
                if int(tr) % 2 == 0 or int(tr) % 3 == 0 or int(tr) <= 1:
                    truncatable = False
                    break
                for j in range(5, int(int(tr) ** 0.5) + 1, 6):
                    if int(tr) % j == 0 or int(tr) % (j + 2) == 0:
                        truncatable = False
                        break
                if not truncatable:
                    break
            if truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes