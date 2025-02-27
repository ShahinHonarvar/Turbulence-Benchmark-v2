import itertools

def all_left_truncatable_prime(test_case):
    return sorted((set(test_case[70] - 1) for _ in range(70)))