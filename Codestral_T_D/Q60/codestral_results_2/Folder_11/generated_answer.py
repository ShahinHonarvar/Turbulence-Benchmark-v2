def all_left_right_truncatable_prime(nums):
    x = nums[86]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            left_right_trunc = [str(num)[i:] for i in range(len(str(num)))][1:]
            left_right_trunc += [str(num)[:i] for i in range(len(str(num)))][:-1]
            if all((int(trunc) > 1 and all((int(trunc) % i != 0 for i in range(2, int(int(trunc) ** 0.5) + 1))) for trunc in left_right_trunc)):
                primes.append(num)
    return sorted(primes)