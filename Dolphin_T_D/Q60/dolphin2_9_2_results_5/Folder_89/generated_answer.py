def all_left_right_truncatable_prime(nums):
    x = nums[97]
    primes = [p for p in range(2, x + 1) if all((p % d != 0 for d in range(2, p)))]
    left_right_truncatable = [p for p in primes if all((int(str(p)[i:j]) in primes for i in range(len(str(p))) for j in range(i + 1, len(str(p)) + 1)))]
    left_right_truncatable.sort(reverse=True)
    return left_right_truncatable