def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        numbers = [int(n)]
        while len(numbers[-1]) > 1:
            numbers.append(int(numbers[-1][1:]))
        return all(map(is_prime, numbers))
    x = numbers[57]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if is_left_truncatable(i)][::-1])