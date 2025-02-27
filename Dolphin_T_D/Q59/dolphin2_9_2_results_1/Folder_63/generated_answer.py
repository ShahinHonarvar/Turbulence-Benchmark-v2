def all_left_truncatable_prime(numbers_tuple):

    def is_left_truncatable(n):
        return all((int(str(n)[i:]) == 0 or is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))

    def is_prime(n):
        if n < 2:
            return False
        for number in range(2, int(n ** 0.5) + 1):
            if n % number == 0:
                return False
        return True
    numbers = [i for i in range(numbers_tuple[88])]
    return sorted([i for i in numbers if is_left_truncatable(i) and is_prime(i)], ascending=True)