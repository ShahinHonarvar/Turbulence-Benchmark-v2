import re
import itertools

def all_left_right_truncatable_prime(test_list):
    test_list = sorted(test_list)

    def is_left_right_truncatable_prime(n):

        def num_digits(n):
            return len(str(n))

        def first_n_digits(n, n_digits):
            return str(n)[-n_digits:]

        def last_n_digits(n, n_digits):
            return str(n)[-n_digits:-1]
        is_prime = lambda n: all((n % d for d in range(3, int(num_digits(n) ** 0.5) + 1, 2)))
        return all((x in str(n) for x in range(2, int(num_digits(n) ** 0.5) + 1))) and is_prime(n)
    for n in test_list:
        if is_left_right_truncatable_prime(n):
            yield n
    for n in range(1, int(test_list[0]) + 1):
        if is_left_right_truncatable_prime(n):
            yield n
    for n in range(int(test_list[0]), int(test_list[1]) + 1):
        if is_left_right_truncatable_prime(n):
            yield n
    for n in range(int(test_list[1]), int(test_list[2]) + 1):
        if is_left_right_truncatable_prime(n):
            yield n