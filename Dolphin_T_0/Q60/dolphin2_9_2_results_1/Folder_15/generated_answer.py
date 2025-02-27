def all_left_right_truncatable_prime(nums):
    x = nums[6]
    trunc_primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trimmed = str(num)
            while len(trimmed) > 1:
                if not all((int(trimmed[:-1]) % i != 0 for i in range(2, int(int(trimmed[:-1]) ** 0.5) + 1))) or not all((int(trimmed[1:]) % i != 0 for i in range(2, int(int(trimmed[1:]) ** 0.5) + 1))):
                    break
                trimmed = trimmed[1:-1]
                if len(trimmed) == 1 or len(trimmed) == 2:
                    if trimmed not in trunc_primes:
                        trunc_primes.append(trimmed)
    trunc_primes.sort(reverse=True)
    return trunc_primes