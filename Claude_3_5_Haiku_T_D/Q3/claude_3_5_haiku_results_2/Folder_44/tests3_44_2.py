from Q3.claude_3_5_haiku_results_2.Folder_44.generated_answer import all_pos_ints_inclusive


def test_large_range():
    large_list = list(range(1, 68 + 1000))
    expected_list = large_list[13:68 + 1]
    assert all_pos_ints_inclusive(large_list) == expected_list


def test_minimal_range():
    minimal_list = list(range(1, 68 + 2))
    expected_list = minimal_list[13:68 + 1]
    assert all_pos_ints_inclusive(minimal_list) == expected_list


def test_even_range():
    even_list = [2 * i for i in range(1, 68 + 2)]
    expected_list = even_list[13:68 + 1]
    assert all_pos_ints_inclusive(even_list) == expected_list


def test_negative_range():
    neg_list = [i for i in range(0, -68 - 2, -1)]
    assert all_pos_ints_inclusive(neg_list) == []


def test_zero_range():
    zero_list = [0 for i in range(0, (68 + 2) * 10)]
    assert all_pos_ints_inclusive(zero_list) == []


def test_range_size():
    initial_list = [i for i in range(-100, 68 + 10)]
    assert len(all_pos_ints_inclusive(initial_list)) < len(initial_list)


def test_range_sum():
    initial_list = [i for i in range(0, 68 + 10)]
    assert sum(all_pos_ints_inclusive(initial_list)) >= 0


def test_ones_range_sum():
    ones_list = [1 for i in range(0, 68 + 2)]
    assert sum(all_pos_ints_inclusive(ones_list)) == 68 - 13 + 1
        