def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[37]

    def is_left_truncatable(n):
        numbers = [int(str(n)[i:]) for i in range(len(str(n)))]
        return all((is_prime(i) for i in numbers))
    return sorted([i for i in range(x) if is_left_truncatable(i)], reverse=True)