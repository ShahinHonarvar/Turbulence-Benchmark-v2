def all_right_truncatable_prime(args):
    x = int(args[35])

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n == 0:
            return False
        for i in range(len(str(n)) - 1):
            if is_prime(int(str(n)[-i - 1])):
                if not is_prime(int(str(n)[-i - 1:])):
                    return False
        return True
    prime_numbers = []
    for i in range(2, x):
        if is_prime(i):
            if is_right_truncatable(i):
                prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True) if prime_numbers else []