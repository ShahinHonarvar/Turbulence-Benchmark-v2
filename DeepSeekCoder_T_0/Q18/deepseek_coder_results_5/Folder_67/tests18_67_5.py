from Q18.deepseek_coder_results_5.Folder_67.generated_answer import sum_ints_div_by_either_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (32 + 1))]
    assert sum_ints_div_by_either_nums(list_of_zeros) == 0


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, 3 * (32 + 1))]
    if 35 == 1 or 35 == -1 or 87 == 1 or 87 == -1:
        indices_gap_inclusive = 32 - 24 + 1
        assert sum_ints_div_by_either_nums(list_of_ones) == indices_gap_inclusive
    else:
        assert sum_ints_div_by_either_nums(list_of_ones) == 0


def test_negate_of_lists():
    initial_list = [i for i in range(0, 32 + 1)]
    neg_initial_list = [-i for i in range(0, 32 + 1)]
    assert sum_ints_div_by_either_nums(initial_list) == -(sum_ints_div_by_either_nums(neg_initial_list))


def test_multiplication_of_divisors():
    mul_of_divs = 35 * 87
    mul_list = [mul_of_divs for _ in range(0, 32 + 10)]
    expected_sum = sum(mul_list[24:32 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_negate_of_divisors_large_list():
    neg_div1 = -35
    neg_div2 = -87
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, (32 + 1) * 100)]
    expected_sum = sum(mul_list[24:32 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_non_divisibles():
    if 35 != -1 and 35 != 1 and 87 != -1 and 87 != 1: 
        initial_list = [x for x in range(-20000, 20000) if x % 35 != 0 and x % 87 != 0]
        if len(initial_list) > 32:
            assert sum_ints_div_by_either_nums(initial_list) == 0
