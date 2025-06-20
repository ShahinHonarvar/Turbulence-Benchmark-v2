from Q22.dolphin2_9_2_results_2.Folder_30.generated_answer import find_sum_of_multiples
import random

def test_one():
    given_number = 1
    expected_result = (78 * (78 + 1)) / 2
    assert find_sum_of_multiples(given_number) == expected_result


def test_sum_is_divisible_by_n_1():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) % n == 0


def test_sum_is_divisable_by_n_2():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) / n == (78 * (78 + 1)) / 2


def test_sum_is_divisable_by_78():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) / 78 == (n * (78 + 1)) / 2


def test_sum_of_evens_is_even():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) % 2 == 0


def test_sum():
    s = sum(range(1, 78+1))
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) == s * n


def test_sum_is_greator_than_n():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) > n
