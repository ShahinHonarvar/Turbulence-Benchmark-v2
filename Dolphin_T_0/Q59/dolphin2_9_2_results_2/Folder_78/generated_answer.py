def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        digits = str(n)
        for i in range(1, len(digits)):
            if not is_prime(int(digits[i:])):
                return False
        return True
    return sorted([n for n in range(numbers[2]) if is_left_truncatable(n) and is_prime(n)])

def test():
    print(all_left_truncatable_prime((555, 1234, 2000)))