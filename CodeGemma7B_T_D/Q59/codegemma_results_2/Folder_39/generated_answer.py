from itertools import product, count
from math import log, sqrt

def left_truncatable_prime(n):
    """
  n: an integer
  return: True if n is left-truncatable prime, False otherwise
  """

    def is_prime(n):
        return not any((i for i in range(2, n) if n % i == 0))
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def test_left_truncatable_prime():
    test_cases = [(1, False), (23, False), (53, True), (4123, False), (547, True), (496231, True), (371, True), (987, False), (37027, True), (3702729, False), (1, 30)]
    for case, expected in test_cases:
        actual = left_truncatable_prime(case)
        assert actual == expected, f'{case}: expected {expected}, actual {actual}'