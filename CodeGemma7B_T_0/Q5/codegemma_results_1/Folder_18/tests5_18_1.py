from Q5.codegemma_results_1.Folder_18.generated_answer import all_neg_ints_inclusive


def test_large_range():
    large_list = list(range(0, 49 + 1000))
    assert all_neg_ints_inclusive(large_list) == []


def test_minimal_range():
    minimal_list = list(range(0, 49 + 1))
    assert all_neg_ints_inclusive(minimal_list) == []


def test_even_range():
    even_list = [-2 * i for i in range(1, 49 + 2)]
    expected_list = even_list[35:49 + 1]
    assert all_neg_ints_inclusive(even_list) == expected_list


def test_negative_range():
    neg_list = [i for i in range(-1, -49 - 2, -1)]
    expected_list = neg_list[35:49 + 1]
    assert all_neg_ints_inclusive(neg_list) == expected_list


def test_positive_range():
    pos_list = [i for i in range(1, 49 + 2)]
    assert all_neg_ints_inclusive(pos_list) == []


def test_zero_range():
    zero_list = [0 for i in range(0, (49 + 2) * 10)]
    assert all_neg_ints_inclusive(zero_list) == []


def test_range_size():
    initial_list = [i for i in range(-100, 49 + 10)]
    assert len(all_neg_ints_inclusive(initial_list)) < len(initial_list)


def test_range_sum():
    initial_list = [i for i in range(-1, -49 - 2, -1)]
    assert sum(all_neg_ints_inclusive(initial_list)) < 0


def test_neg_ones_range_sum():
    neg_ones_list = [-1 for i in range(0, 49 + 2)]
    assert sum(all_neg_ints_inclusive(neg_ones_list)) == -(49 - 35 + 1)
