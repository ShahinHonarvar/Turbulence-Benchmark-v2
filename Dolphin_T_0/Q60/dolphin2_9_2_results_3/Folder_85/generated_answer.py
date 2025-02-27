def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        s = int(n ** 0.5) + 1
        for divisor in range(3, s, 2):
            if n % divisor == 0:
                return False
        return True

    def is_left_and_right_truncatable(prime):
        while len(str(prime)) > 2:
            if not is_prime(int(str(prime)[1:-1])):
                return False
            prime = int(str(prime)[1:-1])
        return True
    x = int_tuple[94]
    result = []
    for n in range(2, x + 1):
        if is_left_and_right_truncatable(n) and is_prime(n):
            result.append(n)
    return sorted(result)