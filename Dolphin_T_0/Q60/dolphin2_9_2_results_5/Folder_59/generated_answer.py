def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[84]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if '0' not in str(num):
            trunc = num
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:-1])
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)