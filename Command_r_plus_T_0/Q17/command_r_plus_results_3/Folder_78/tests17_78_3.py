from Q17.command_r_plus_results_3.Folder_78.generated_answer import all_ints_div_by_both_two_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 5 * (69 + 1))]
    expected_list = [0 for i in range(34, 69 + 1)]
    assert all_ints_div_by_both_two_nums(list_of_zeros) == expected_list


def test_multiplication_of_divisors():
    mul_of_divisors = 19 * 32
    mul_list = [mul_of_divisors for _ in range(0, 69 + 1)]
    expected_list = [mul_of_divisors for _ in range(34, 69 + 1)]
    assert all_ints_div_by_both_two_nums(mul_list) == expected_list


def test_negate_of_lists():
    initial_list = [i for i in range(0, 69 + 1)]
    neg_initial_list = [-i for i in range(0, 69 + 1)]
    expected_list = [-i for i in all_ints_div_by_both_two_nums(neg_initial_list)]
    assert all_ints_div_by_both_two_nums(initial_list) == expected_list


def test_negate_of_divisors():
    neg_div1 = -19
    neg_div2 = -32
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, 69 + 1)]
    expected_list = [mul_of_negs for _ in range(34, 69 + 1)]
    assert all_ints_div_by_both_two_nums(mul_list) == expected_list


def test_lengths():
    initial_list = [x for x in range(0, 69 + 1)]
    expected_list = all_ints_div_by_both_two_nums(initial_list)
    assert len(expected_list) <= len(initial_list)


def test_sums():
    initial_list = [x for x in range(0, 69 + 1)]
    expected_list = all_ints_div_by_both_two_nums(initial_list)
    assert sum(expected_list) <= sum(initial_list)


def test_non_divisibles_1():
    if 19 != -1 and 19 != 1:
        initial_list = [x for x in range(-20000, 20000) if x % 19 != 0]
        assert all_ints_div_by_both_two_nums(initial_list) == []


def test_non_divisibles_2():
    if 32 != -1 and 32 != 1:
        initial_list = [x for x in range(-20000, 20000) if x % 32 != 0]
        assert all_ints_div_by_both_two_nums(initial_list) == []
