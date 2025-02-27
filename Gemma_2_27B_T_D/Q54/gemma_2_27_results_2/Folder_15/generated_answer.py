def all_right_truncatable_prime(nums):
    x = nums[6]
    primes = []
    for num in range(x, 0, -1):
        prime = True
        num_str = str(num)
        if num_str[-1] == '0':
            continue
        for i in range(2, int(num_str ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            truncatable = True
            for j in range(len(num_str) - 1, 0, -1):
                trunc = int(num_str[:j])
                if trunc < 2:
                    truncatable = False
                    break
                for k in range(2, int(trunc ** 0.5) + 1):
                    if trunc % k == 0:
                        truncatable = False
                        break
                if not truncatable:
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)