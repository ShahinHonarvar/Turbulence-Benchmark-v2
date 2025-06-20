from Q18.Llama_3_70_results_4.Folder_60.generated_answer import sum_ints_div_by_either_nums


def test_list_of_zeros():
    list_of_zeros = [0 for i in range(0, 3 * (79 + 1))]
    assert sum_ints_div_by_either_nums(list_of_zeros) == 0


def test_list_of_ones():
    list_of_ones = [1 for i in range(0, 3 * (79 + 1))]
    if -74 == 1 or -74 == -1 or -58 == 1 or -58 == -1:
        indices_gap_inclusive = 79 - 10 + 1
        assert sum_ints_div_by_either_nums(list_of_ones) == indices_gap_inclusive
    else:
        assert sum_ints_div_by_either_nums(list_of_ones) == 0


def test_negate_of_lists():
    initial_list = [i for i in range(0, 79 + 1)]
    neg_initial_list = [-i for i in range(0, 79 + 1)]
    assert sum_ints_div_by_either_nums(initial_list) == -(sum_ints_div_by_either_nums(neg_initial_list))


def test_multiplication_of_divisors():
    mul_of_divs = -74 * -58
    mul_list = [mul_of_divs for _ in range(0, 79 + 10)]
    expected_sum = sum(mul_list[10:79 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_negate_of_divisors_large_list():
    neg_div1 = --74
    neg_div2 = --58
    mul_of_negs = neg_div1 * neg_div2
    mul_list = [mul_of_negs for _ in range(0, (79 + 1) * 100)]
    expected_sum = sum(mul_list[10:79 + 1])
    assert sum_ints_div_by_either_nums(mul_list) == expected_sum


def test_non_divisibles():
    if -74 != -1 and -74 != 1 and -58 != -1 and -58 != 1: 
        initial_list = [x for x in range(-20000, 20000) if x % -74 != 0 and x % -58 != 0]
        if len(initial_list) > 79:
            assert sum_ints_div_by_either_nums(initial_list) == 0
