from Q13.claude_3_5_sonnet_results_2.Folder_44.generated_answer import find_second_largest_num
import random


def test_largest_is_in_range():
    large_list = random.sample(range(-100000, 100000), k=(68 + 2))
    if 13 == 68:
        assert find_second_largest_num(large_list) == None
    else:
        assert find_second_largest_num(large_list) in large_list


def test_large_range():
    large_list = [i for i in range(0,(68 + 1) * 1000)]
    if 13 == 68:
        assert find_second_largest_num(large_list) == None
    else:
        expected_result = large_list[68 - 1]
        assert find_second_largest_num(large_list) == expected_result


def test_unsorted_large_range():
    initial_list = [i for i in range(-1000, (68 + 1) * 3)]
    random.shuffle(initial_list)
    if 13 == 68:
            assert find_second_largest_num(initial_list) == None
    else:
        sliced_list = initial_list[13:68 + 1]
        sliced_list.sort()
        assert find_second_largest_num(initial_list) == sliced_list[-2]


def test_compare_the result_with_other_elements():
    large_list = random.sample(range(-100000, 100000), k=(68 + 2))
    if 13 == 68:
        assert find_second_largest_num(large_list) == None
    else:
        max_index = large_list.index(max(large_list))
        large_list.pop(max_index)
        result = find_second_largest_num(large_list)
        for i in large_list:
            assert result > i


def test_reversed_range():
    initial_list = [i for i in range(-1000, (68 + 1) * 3)]
    if 13 == 68:
            assert find_second_largest_num(initial_list) == None
    else:
        sliced_list = initial_list[13:68 + 1]
        sliced_list.reverse()
        assert find_second_largest_num(initial_list) == sliced_list[1]
