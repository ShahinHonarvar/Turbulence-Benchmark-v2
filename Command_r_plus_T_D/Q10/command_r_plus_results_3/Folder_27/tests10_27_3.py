from Q10.command_r_plus_results_3.Folder_27.generated_answer import all_odd_ints_exclusive


def test_odd_same_number():
    for n in range(-11,12,2):
        n_list = [n for _ in range(0, (49 + 1) * 10)]
        assert all_odd_ints_exclusive(n_list) == n_list[28 + 1: 49]


def test_odd_range():
    odd_list = list(range(1, (49 + 1) * 10, 2))
    assert all_odd_ints_exclusive(odd_list) == odd_list[28 + 1: 49]


def test_even_range():
    even_list = list(range(0, (49 + 1) * 10, 2))
    assert all_odd_ints_exclusive(even_list) == []


def test_all_zero_range():
    zero_list = [0 for _ in range(0,(49 + 1) * 5)]
    assert all_odd_ints_exclusive(zero_list) == []


def test_all_one_range():
    initial_list = [1 for _ in range(0, 49 + 10)]
    assert all_odd_ints_exclusive(initial_list) == initial_list[28 + 1: 49]


def test_all_negative_one_range():
    initial_list = [-1 for _ in range(0, 49 + 10)]
    assert all_odd_ints_exclusive(initial_list) == initial_list[28 + 1: 49]


def test_range_size():
    initial_list = list(range(-1000, (49 + 1) * 3))
    assert len(all_odd_ints_exclusive(initial_list)) < len(initial_list)


def test_range_sum_positive_odds():
    initial_list = list(range(1, 49 + 10))
    assert sum(all_odd_ints_exclusive(initial_list)) >= 0


def test_range_sum_negative_odds():
    initial_list = list(range(-1, -49 - 10, -1))
    assert sum(all_odd_ints_exclusive(initial_list)) <= 0


def test_each_num_is_odd():
    initial_list = list(range(-100, 49 + 50))
    result_list  = all_odd_ints_exclusive(initial_list)
    for i in result_list:
        assert i % 2 != 0
