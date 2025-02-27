def all_left_truncatable_prime(nums):
    x = nums[126]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(x - 1, 1, -1):
        num_str = str(i)
        flag = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[j:])):
                flag = False
                break
        if flag and '0' not in num_str:
            primes.append(i)
    return sorted(primes, reverse=True)