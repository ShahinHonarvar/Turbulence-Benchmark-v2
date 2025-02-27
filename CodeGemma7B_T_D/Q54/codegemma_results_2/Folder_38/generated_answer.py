import sympy as sm
    import math

def all_right_truncatable_prime(tu):
    x = int(tu[28])

    def get_next_sequence_number(number):
        str_number = str(number)
        next_sequence_number = int(str_number[:-1] + str_number[-1:])
        return next_sequence_number

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def is_right_truncatable_prime(number):
        sequence_number = get_next_sequence_number(number)
        while sequence_number <= number:
            if not is_prime(sequence_number):
                return False
            sequence_number = get_next_sequence_number(sequence_number)
        return is_prime(number)
    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
    right_truncatable_primes.sort()
    return right_truncatable_primes