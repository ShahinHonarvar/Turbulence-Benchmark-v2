def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        if n != 1 and n != 0:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    x = int_tuple[36]
    left_right_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        while len(num_str) > 1 and is_prime(int(num_str)):
            if len(num_str) == 2:
                left_right_primes.append(int(num_str))
                break
            else:
                num_str = num_str[1:-1]
    return sorted(left_right_primes, reverse=True)