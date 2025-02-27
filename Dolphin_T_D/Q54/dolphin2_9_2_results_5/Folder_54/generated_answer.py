def all_right_truncatable_prime(a_tuple):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        numbers = [n]
        last_digit = n % 10
        while n:
            n //= 10
            numbers.append(n)
        return all((is_prime(num) for num in numbers))
    x = a_tuple[88]
    return sorted([num for num in range(2, x) if is_right_truncatable_prime(num)], reverse=True)