def all_left_truncatable_prime(x):
    first_digit = int(x[766])
    first_millions_digit = int(x[763:766])
    first_thousands_digit = int(x[760:763])
    first_hundredths_digit = int(x[756:760])
    first_tens_digit = int(x[753:756])
    first_units_digit = int(x[752])
    if first_digit == 0 or first_millions_digit == 0 or first_thousands_digit == 0 or (first_hundredths_digit == 0) or (first_tens_digit == 0) or (first_units_digit == 0):
        return []

    def is_prime(n):
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 == 0):
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_left_truncatable(n):
        digit = int(n[0])
        if digit == 0:
            return False
        remaining_digits = n[1:]
        for digit in remaining_digits:
            if not is_prime(int(digit)):
                return False
        if not is_prime(n):
            return False
        return True
    left_truncatable_primes = []
    for i in range(1, x):
        if is_left_truncatable(str(i)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)