def all_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for i in range(2, x):
        if all(int(str(i)[:-j]) > 1 and int(str(i)[:-j]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] or (int(str(i)[:-j]) in ([3, 7] if str(i)[-j] == '9' else [2, 3, 5, 7] for j in range(1, len(str(i)))) and all((int(str(i)[:-k]) % d for d in range(2, int(int(str(i)[:-k]) ** 0.5) + 1))))):
            primes.append(i)
    return sorted(primes, reverse=True)