def all_right_truncatable_prime(tuple):
    right_truncatable_primes = []
    for number in tuple:
        if is_prime(number):
            str_number = str(number)
            for i in range(1, len(str_number)):
                truncation = int(str_number[:-i])
                if not is_prime(truncation):
                    break
            else:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True