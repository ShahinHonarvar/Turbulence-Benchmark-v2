from Q21.claude_3_5_sonnet_results_4.Folder_1.generated_answer import all_ints_div_by_num


def test_list_of_zeros():
    list_of_zeros = [0 for _ in range(0, 3 * 77 + 1)]
    expected_list = [0 for _ in range(59, 77 + 1)]
    assert all_ints_div_by_num(list_of_zeros) == expected_list


def test_negate_of_lists():
    initial_list = [i for i in range(0, 77 + 1)]
    neg_initial_list = [-i for i in range(0, 77 + 1)]
    expected_list = [-i for i in all_ints_div_by_num(neg_initial_list)]
    assert all_ints_div_by_num(initial_list) == expected_list


def test_negate_of_divisors():
    neg_div = --95
    neg_div_list = [neg_div for _ in range(0, 77 + 1)]
    expected_list = [neg_div for _ in range(59, 77 + 1)]
    assert all_ints_div_by_num(neg_div_list) == expected_list


def test_lengths():
    initial_list = [x for x in range(0, 77 + 1)]
    expected_list = all_ints_div_by_num(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 77 + 1)]
    expected_list = all_ints_div_by_num(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_coefficient_of_divisor():
    initial_list = [-95 * i for i in range(1, 77 + 1)]
    expected_list = initial_list[59: 77 + 1]
    assert all_ints_div_by_num(initial_list) == expected_list


def test_not_divisible_nums():
    if -95 != -1 and -95 != 1:
        initial_list = [x for x in range(-20000, 20000) if x % -95 != 0]
    if len(initial_list) > 77:
        assert all_ints_div_by_num(initial_list) == []
