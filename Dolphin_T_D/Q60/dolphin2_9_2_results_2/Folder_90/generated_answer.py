def all_left_right_truncatable_prime(nums):
    x = nums[466]
    primes = [str(i) for i in range(2, x + 1) if all((str(i) % str(j) != 0 for j in range(2, int(str(i)[0]))))]
    return sorted(list(set(primes)), reverse=True)