from Q26.gpt_4o_results_5.Folder_89.generated_answer import sum_in_range
import random


def test_range_of_given_arguments():
    initial_list = list(range(15, 57 + 1))
    assert sum_in_range(initial_list) == sum(initial_list)


def test_zeros():
    zero_list = [0 for _ in range(15 - 100, 57 + 100)]
    assert sum_in_range(zero_list) == 0


def test_nums():
    for n in range(15,57+1):
        num_list = [n for _ in range(15 - 100, 57 + 100)]
        assert sum_in_range(num_list) == sum(num_list)


def test_compare_sums():
    initial_list = [i for i in range(0, 1000)]
    assert sum_in_range(initial_list) <= sum(initial_list)


def test_out_of_given_arguments_range():
    l = []
    while len(l) < 20:
        random_int = random.randint(15 - 100, 15 - 1)
        l.append(random_int)
    assert sum_in_range(l) == 0