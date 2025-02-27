def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable(prime):
        original = prime
        while prime > 0:
            if not is_prime(prime):
                return False
            prime //= 10
        return original != 0
    threshold = numbers[54]
    result = []
    for num in range(2, threshold):
        if is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)