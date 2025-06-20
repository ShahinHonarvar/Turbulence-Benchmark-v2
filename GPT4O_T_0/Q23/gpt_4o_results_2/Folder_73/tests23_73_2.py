from Q23.gpt_4o_results_2.Folder_73.generated_answer import find_divisors_in_range
import random


def test_one():
    if 46 <= 1 <= 89:
        assert find_divisors_in_range(1) == [1]
    else:
        assert find_divisors_in_range(1) == []


def test_one_is_among_result():
    for n in range(2, 21):
        if 46 <= 1 <= 89:
            assert 1 in find_divisors_in_range(n)
        else:
            assert not 1 in find_divisors_in_range(n)


def test_divisors_less_than_equal_n():
    for n in range(46, 89 + 1):
        divisors_list = find_divisors_in_range(n)
        for divisor in divisors_list:
            assert divisor <= n


def test_divisors_subsets():
    for n in range(46, 89 + 1):
        divisors_list = find_divisors_in_range(n)
        for divisor in divisors_list:
            assert set(find_divisors_in_range(divisor)) <= set(divisors_list)


# This test executes if the upperbound is positive (i.e. if 89 > 0).
def test_the_first_prime_succeeding_upperbound():
    if 89 > 0:
        n = 0
        for i in range(89 + 1, 1000000):
            flag = False
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if not flag:
                n = i
                break
        if 46 > 1:
            assert find_divisors_in_range(n) == []
        else:
            assert find_divisors_in_range(n) == [1]
        

# This test executes if the upperbound is not positive (i.e. if 89 < 1).
def test_if_upperbound_is_not_positive():
    if 89 < 1:
        n = random.randint(10, 1000)
        assert find_divisors_in_range(n) == []


# This test executes if the upperbound is positive (i.e. if 89 > 0).
def test_nums_between_range():
    if 89 > 0:
        for n in range(46, 89 + 1):
            if n >= 1:
                assert n in find_divisors_in_range(n)
            else:
                assert find_divisors_in_range(n) == []
        