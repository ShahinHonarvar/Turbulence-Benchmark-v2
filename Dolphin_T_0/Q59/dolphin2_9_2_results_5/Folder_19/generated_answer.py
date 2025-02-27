def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        return n <= 0 or (all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))) and is_prime(n))

    def is_prime(n):
        if n % 2 == 0 or n == 1:
            return n == 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers[67]
    return sorted([n for n in range(1, x) if is_left_truncatable_prime(n)], reverse=True)