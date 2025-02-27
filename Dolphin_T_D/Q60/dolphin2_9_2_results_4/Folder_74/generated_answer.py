def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digits(n):
        if n // 10 == 0:
            return []
        return [n // 10, n % 10]
    x = numbers[36]
    primes = []
    for num in range(2, x + 1):
        if str(num).count('0') != 0:
            continue
        for i in range(len(str(num)) - 2):
            left = int(str(num)[i + 1:])
            right = int(str(num)[:-i - 1])
            if not (is_prime(left) and is_prime(right) and is_prime(num)):
                break
            if i == len(str(num)) - 3:
                primes.append(num)
    return sorted(primes)