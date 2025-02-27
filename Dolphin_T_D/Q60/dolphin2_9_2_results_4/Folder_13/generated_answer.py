def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    primes = []
    x = numbers[784]
    for i in range(x, 1, -1):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:-1])
            else:
                primes.append(i)
    return primes