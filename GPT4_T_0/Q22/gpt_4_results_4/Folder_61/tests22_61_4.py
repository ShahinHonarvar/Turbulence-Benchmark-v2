from Q22.gpt_4_results_4.Folder_61.generated_answer import find_sum_of_multiples
import random

def test_one():
    given_number = 1
    expected_result = (5 * (5 + 1)) / 2
    assert find_sum_of_multiples(given_number) == expected_result


def test_sum_is_divisible_by_n_1():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) % n == 0


def test_sum_is_divisable_by_n_2():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) / n == (5 * (5 + 1)) / 2


def test_sum_is_divisable_by_5():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) / 5 == (n * (5 + 1)) / 2


def test_sum_of_evens_is_even():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) % 2 == 0


def test_sum():
    s = sum(range(1, 5+1))
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) == s * n


def test_sum_is_greator_than_n():
    n = random.randint(1, 1000)
    assert find_sum_of_multiples(n) > n
