def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[31]
    trunc_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_trunc_prime = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_trunc_prime = False
                break
            temp = int(str(temp)[1:])
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_trunc_prime = False
                break
            temp = int(str(temp)[:-1])
        if is_trunc_prime:
            trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)