from Q24.command_r_plus_results_1.Folder_90.generated_answer import sum_of_divisors_in_range
import random

def test_one():
    if 451 <= 1 <= 973:
        assert sum_of_divisors_in_range(1) == 1
    else:
        assert sum_of_divisors_in_range(1) == 0


def test_sum_greater_than_equal_num():
    for n in range(451, 973 + 1):
        assert n <= sum_of_divisors_in_range(n)


def test_sum_of_divisors_subsets():
    for n in range(451, 973 + 1):
        divisors_list = [i for i in range(1, n + 1) if n % i == 0 and 451 <= i <= 973]
        for divisor in divisors_list:
            assert sum_of_divisors_in_range(divisor) <= sum_of_divisors_in_range(n)


# This test executes if the upperbound is positive (i.e. if 973 > 0).
def test_the_first_prime_succeeding_upperbound():
    if 973 > 0:
        n = 0
        for i in range(973 + 1, 1000000):
            flag = False
            for j in range(2, i):
                if i % j == 0:
                    flag = True
                    break
            if not flag:
                n = i
                break
        if 451 > 1:
            assert sum_of_divisors_in_range(n) == 0
        else:
            assert sum_of_divisors_in_range(n) == 1
        

# This test executes if the upperbound is not positive (i.e. if 973 < 1).
def test_if_upperbound_is_not_positive():
    if 973 < 1:
        n = random.randint(10, 1000)
        assert sum_of_divisors_in_range(n) == 0


# This test executes if the upperbound is positive (i.e. if 973 > 0).
def test_sum_range():
    if 973 > 0:
        for n in range(451, 973 + 1):
            if n >= 1:
                assert sum_of_divisors_in_range(n) > 0
            else:
                assert sum_of_divisors_in_range(n) == 0
        