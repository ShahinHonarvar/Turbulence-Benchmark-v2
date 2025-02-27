def all_left_right_truncatable_prime(nums):
    x = nums[42]
    primes = [2, 3, 5, 7]
    if x <= 9:
        return [i for i in primes if i <= x]
    else:
        for i in range(1, x):
            if all((i % p != 0 for p in primes)) and i % 2 != 0 and all((int(str(i)[j:j + 2]) % 2 != 0 for j in range(len(str(i)) - 1))):
                primes.append(i)
        return [i for i in primes if i <= x]