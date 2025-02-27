def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(prime):
        str_prime = str(prime)
        while len(str_prime) > 2:
            str_prime = str_prime[1:-1]
            if not is_prime(int(str_prime)):
                return False
        return True
    x = tup[41]
    result = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)