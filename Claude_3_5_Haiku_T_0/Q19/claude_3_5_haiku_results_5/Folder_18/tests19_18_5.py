from Q19.claude_3_5_haiku_results_5.Folder_18.generated_answer import all_ints_not_div_by_num


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (98 + 1))]
    assert all_ints_not_div_by_num(list_of_zeros) == []


def test_negate_of_lists():
    initial_list = [i for i in range(0, 98 + 1)]
    neg_initial_list = [-i for i in range(0, 98 + 1)]
    expected_list = [-i for i in all_ints_not_div_by_num(neg_initial_list)]
    assert all_ints_not_div_by_num(initial_list) == expected_list


def test_negate_of_divisors():
    neg_div = -41
    neg_div_list = [neg_div for _ in range(0, 98 + 1)]
    assert all_ints_not_div_by_num(neg_div_list) == []


def test_compare_neg_divisor():
    initial_list = [i for i in range(0, 98 + 1)]
    neg_div = -41
    neg_div_result_list = [i for i in initial_list[35 + 1: 98] if i % neg_div != 0]
    assert all_ints_not_div_by_num(initial_list) == neg_div_result_list


def test_lengths():
    initial_list = [x for x in range(0, 98 + 1)]
    expected_list = all_ints_not_div_by_num(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 98 + 1)]
    expected_list = all_ints_not_div_by_num(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_coefficient_of_divisor():
    for n in range(-10,11):
        initial_list = [41 * n for _ in range(0, 98 + 1)]
        assert all_ints_not_div_by_num(initial_list) == []
        

def test_divisibles():
    initial_list = [x for x in range(-20000, 20000) if x % 41 == 0]
    if len(initial_list) > 98:
        assert all_ints_not_div_by_num(initial_list) == []