def all_left_truncatable_prime(numbers):
    x = numbers[429]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return is_left_truncatable_prime(int(str(n)[1:]))
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result