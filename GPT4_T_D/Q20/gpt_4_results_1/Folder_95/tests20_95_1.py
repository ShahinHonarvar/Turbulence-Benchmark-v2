from Q20.gpt_4_results_1.Folder_95.generated_answer import find_n_th_smallest_num
import random
import math


def test_n_th_smallest_is_in_range():
    large_list = [i for i in range(0,(48 + 1) * 1000)]
    assert find_n_th_smallest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(48 + 1) * 1000)]
    expected_result = large_list[44:48 + 1][5 - 1]
    assert find_n_th_smallest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, 48 + 1000)]
    random.shuffle(initial_list)
    sliced_list = initial_list[44:48 + 1]
    sliced_list.sort()
    assert find_n_th_smallest_num(initial_list) == sliced_list[5 - 1]


def test_reversed_range():
    initial_list = [i for i in range(-100, 48 + 100)]
    sliced_list = initial_list[44:48 + 1]
    sliced_list.reverse()
    assert find_n_th_smallest_num(initial_list) == sliced_list[-5]


def test_float_numbers():
    initial_list = [math.sqrt(i) for i in range(1, 48 + 10)]
    expected_result = initial_list[44:48 + 1][5 - 1]
    assert find_n_th_smallest_num(initial_list) == expected_result


def test_unsorted_float_numbers():
    initial_list = [math.sqrt(i) for i in range(1, 48 + 10)]
    random.shuffle(initial_list)
    sliced_list = initial_list[44:48 + 1]
    sliced_list.sort()
    assert find_n_th_smallest_num(initial_list) == sliced_list[5 - 1]

