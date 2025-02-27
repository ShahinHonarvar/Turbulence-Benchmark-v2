def all_right_truncatable_prime(nums):
    x = nums[54]
    primes = [2]
    for num in range(3, x, 2):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted([p for p in primes if all([int(str(p)[:i]) in primes for i in range(len(str(p)), 0, -1)])])[::-1]