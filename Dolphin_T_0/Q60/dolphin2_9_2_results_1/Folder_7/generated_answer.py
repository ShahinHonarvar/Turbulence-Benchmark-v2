def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[803]
    left_right_truncatable_prime_numbers = []

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n != 0 and n != 1:
            if not is_prime(n):
                return False
            n = int(str(n)[-1])
            n = int(str(n)[1:])
        return True
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            left_right_truncatable_prime_numbers.append(i)
    return sorted(left_right_truncatable_prime_numbers)