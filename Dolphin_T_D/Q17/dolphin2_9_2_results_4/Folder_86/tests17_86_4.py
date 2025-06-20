from Q17.dolphin2_9_2_results_4.Folder_86.generated_answer import all_ints_div_by_both_two_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 5 * (79 + 1))]
    expected_list = [0 for i in range(54, 79 + 1)]
    assert all_ints_div_by_both_two_nums(list_of_zeros) == expected_list


def test_multiplication_of_divisors():
    mul_of_divisors = 54 * 28
    mul_list = [mul_of_divisors for _ in range(0, 79 + 1)]
    expected_list = [mul_of_divisors for _ in range(54, 79 + 1)]
    assert all_ints_div_by_both_two_nums(mul_list) == expected_list


def test_negate_of_lists():
    initial_list = [i for i in range(0, 79 + 1)]
    neg_initial_list = [-i for i in range(0, 79 + 1)]
    expected_list = [-i for i in all_ints_div_by_both_two_nums(neg_initial_list)]
    assert all_ints_div_by_both_two_nums(initial_list) == expected_list


def test_negate_of_divisors():
    neg_div1 = -54
    neg_div2 = -28
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, 79 + 1)]
    expected_list = [mul_of_negs for _ in range(54, 79 + 1)]
    assert all_ints_div_by_both_two_nums(mul_list) == expected_list


def test_lengths():
    initial_list = [x for x in range(0, 79 + 1)]
    expected_list = all_ints_div_by_both_two_nums(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 79 + 1)]
    expected_list = all_ints_div_by_both_two_nums(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_non_divisibles_1():
    if 54 != -1 and 54 != 1:
        initial_list = [x for x in range(-20000, 20000) if x % 54 != 0]
        assert all_ints_div_by_both_two_nums(initial_list) == []


def test_non_divisibles_2():
    if 28 != -1 and 28 != 1:
        initial_list = [x for x in range(-20000, 20000) if x % 28 != 0]
        assert all_ints_div_by_both_two_nums(initial_list) == []
