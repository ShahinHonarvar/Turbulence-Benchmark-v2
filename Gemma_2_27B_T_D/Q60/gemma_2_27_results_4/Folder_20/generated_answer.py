def all_left_right_truncatable_prime(nums):
    x = nums[100]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        i_str = str(i)
        if '0' in i_str:
            continue
        is_truncatable = True
        for j in range(1, len(i_str)):
            if not is_prime(int(i_str[j:])) or not is_prime(int(i_str[:-j])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(i)
    return sorted(primes, reverse=True)