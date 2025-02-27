def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 126:
        return []
    x = numbers[126]

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

    def no_zero(n):
        return '0' not in str(n)

    def truncatable_from_both_sides(n):
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and no_zero(num):
            if truncatable_from_both_sides(num):
                left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes