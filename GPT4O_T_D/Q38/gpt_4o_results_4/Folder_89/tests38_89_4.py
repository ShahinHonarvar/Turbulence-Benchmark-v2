from Q38.gpt_4o_results_4.Folder_89.generated_answer import find_subset_of_length_n
import math
import random
import string


def test_smaller_sets():
    set_lengths = {i for i in range(1, 18)}
    for i in set_lengths:
        initial_set = {j for j in range(i)}
        assert find_subset_of_length_n(initial_set) == 0


def test_set_of_length_18_plus_1():
    initial_set = {i for i in range(18+1)}
    assert find_subset_of_length_n(initial_set) == 18+1 
        

def test_largest_subset():
    # This condition is used since the question says the
    # argument should be a set of elements, which means the
    # size of the argument should be greater than 1.
    if 18 >= 2:
        initial_set = {i for i in range(18)}
        assert find_subset_of_length_n(initial_set) == 1


def test_result_smaller_than_number_of_all_subsets():
    initial_set = {i for i in range(18 + 2)}
    number_of_all_subsets = pow(2, len(initial_set))
    assert find_subset_of_length_n(initial_set) < number_of_all_subsets


def test_set_of_strings():
    initial_set = set(string.printable)
    if 18 <= 100:
        assert find_subset_of_length_n(initial_set) == math.comb(len(initial_set), 18)
    else:
        assert find_subset_of_length_n(initial_set) == 0


def test_set_of_float_numbers():
    initial_set = set()
    while len(initial_set) < (18 + 1) + 100:
        initial_set.add(round(random.uniform(-100.0, 100.0),5))
    assert find_subset_of_length_n(initial_set) == math.comb(len(initial_set), 18)


def test_set_of_numbers_strings_bools():
    initial_set = set()
    while len(initial_set) < (18 + 1) + 100:
        initial_set.add(round(random.uniform(-100.0, 100.0),5))
    initial_set |= set(string.printable)
    initial_set |= {True,False}
    assert find_subset_of_length_n(initial_set) == math.comb(len(initial_set), 18)
    