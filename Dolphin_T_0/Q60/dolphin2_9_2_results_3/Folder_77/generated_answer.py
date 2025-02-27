def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    numbers = list(numbers)
    numbers.sort(reverse=True)
    x = numbers[767]

    def remove_digits(n):
        while n > 9 and is_prime(n):
            n = int(n // 10)
        while n > 9 and is_prime(n):
            n = int(n / 10)
        return n

    def is_left_right_truncatable(n):
        m = n
        while m > 9:
            m = remove_digits(m)
            if not is_prime(m):
                return False
        return is_prime(m)
    primes = []
    for num in numbers:
        if is_left_right_truncatable(num):
            primes.append(num)
    return primes