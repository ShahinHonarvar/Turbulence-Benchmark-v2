import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[4]
    left_truncatable_prime = []
    for possible_prime in range(2, x):
        if is_prime(possible_prime):
            str_possible_prime = str(possible_prime)
            while len(str_possible_prime) > 0:
                if not is_prime(int(str_possible_prime)):
                    break
                str_possible_prime = str_possible_prime[1:]
            else:
                left_truncatable_prime.append(possible_prime)
    left_truncatable_prime.sort()
    return left_truncatable_prime