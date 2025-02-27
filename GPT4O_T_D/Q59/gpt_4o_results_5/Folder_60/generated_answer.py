def all_left_truncatable_prime(numbers):

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

    def left_truncate(num):
        num_str = str(num)
        return all((is_prime(int(num_str[i:])) for i in range(len(num_str))))
    x = numbers[87]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num) and left_truncate(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)