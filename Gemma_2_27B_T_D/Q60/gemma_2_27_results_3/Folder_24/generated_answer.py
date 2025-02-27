def all_left_right_truncatable_prime(nums):
    x = nums[65]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] and int(str(num)[:i + 1]) in [2, 3, 5, 7] for i in range(len(str(num))))) and all((int(str(num)[i:]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] and int(str(num)[:i + 1]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] for i in range(len(str(num))))):
            primes.append(num)
    primes.sort(reverse=True)
    return primes