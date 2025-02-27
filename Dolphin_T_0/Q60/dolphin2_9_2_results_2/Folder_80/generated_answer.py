def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[14]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            i_str = str(i)
            while len(i_str) > 2:
                if i_str[1:-1] == '0':
                    break
                i_str = i_str[1:-1]
                if is_prime(int(i_str)):
                    truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True) if truncatable_primes else []