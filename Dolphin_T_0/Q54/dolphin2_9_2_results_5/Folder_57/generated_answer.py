def all_right_truncatable_prime(parameters):

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True
    x = parameters[54]
    prime_numbers = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(prime_numbers, reverse=True) if prime_numbers else []