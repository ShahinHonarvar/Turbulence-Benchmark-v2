def all_right_truncatable_prime(tple):
    x = tple[20]
    right_truncatable_primes = []
    for number in range(999999999, x - 1, -1):
        if is_prime(number):
            for digit in range(1, 10):
                digit_removed_number = number // 10 ** digit
                if not is_prime(digit_removed_number):
                    break
            else:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True