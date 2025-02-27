def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[645]
    result = []
    for n in range(2, x):
        if is_truncatable(n) and is_prime(n):
            result.append(n)
    return sorted(result)