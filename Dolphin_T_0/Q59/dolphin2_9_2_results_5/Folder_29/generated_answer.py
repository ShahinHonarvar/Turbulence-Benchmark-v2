def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        numbers = [int(s) for s in str(n) if s != '0']
        for x in reversed(range(1, len(numbers))):
            if not is_prime(numbers[:x]):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i is 0:
                return False
        return True
    x = numbers[0]
    return sorted([i for i in range(2, x) if is_prime(i) and is_left_truncatable_prime(i)], reverse=True)