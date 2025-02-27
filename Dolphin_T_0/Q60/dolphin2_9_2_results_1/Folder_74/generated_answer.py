def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[36]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if i % 10 == 0 or '0' in str(i):
            continue
        while i > 1:
            if is_prime(i) and (is_prime(int(str(i)[1:-1])) or len(str(i)) == 2):
                left_right_truncatable_primes.append(i)
                break
            i = int(str(i)[1:-1])
    return left_right_truncatable_primes