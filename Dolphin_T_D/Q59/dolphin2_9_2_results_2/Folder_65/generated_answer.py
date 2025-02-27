def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[32]
    left_truncatable_prime_numbers = []
    for i in range(2, x):
        num = i
        while num != 0:
            if not num % 10:
                break
            num = num // 10
            if not is_prime(num):
                break
        else:
            left_truncatable_prime_numbers.append(i)
    return sorted(left_truncatable_prime_numbers)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True