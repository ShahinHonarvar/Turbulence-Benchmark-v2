def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str) - 1, 0, -1):
            if not is_prime(int(num_str[:i])):
                return False
        return True
    x = input_tuple[758]
    primes_list = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes_list)