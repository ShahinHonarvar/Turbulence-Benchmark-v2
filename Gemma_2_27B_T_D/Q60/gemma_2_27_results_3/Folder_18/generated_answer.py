def all_left_right_truncatable_prime(numbers):
    x = numbers[429]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        i_str = str(i)
        if '0' not in i_str and is_prime(i):
            is_truncatable = True
            for j in range(1, len(i_str)):
                if not (is_prime(int(i_str[j:])) and is_prime(int(i_str[:-j]))):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)