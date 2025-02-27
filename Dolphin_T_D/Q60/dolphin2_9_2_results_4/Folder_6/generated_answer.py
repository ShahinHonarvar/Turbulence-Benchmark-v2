def all_left_right_truncatable_prime(numbers):
    x = numbers[74]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n, x):
        n_str = str(n)
        if '0' in n_str:
            return False
        while n >= x:
            if not is_prime(n):
                return False
            n_str = n_str[1:-1]
            n = int(n_str)
        return True
    left_right_truncatable_prime = []
    for n in range(2, x + 1):
        if is_truncatable(n, x):
            left_right_truncatable_prime.append(n)
    return sorted(left_right_truncatable_prime)