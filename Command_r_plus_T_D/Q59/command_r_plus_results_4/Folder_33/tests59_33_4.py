from Q59.command_r_plus_results_4.Folder_33.generated_answer import all_left_truncatable_prime
import random


def test_list_of_all_one_digit_nums():
    for i in range(1,10):
        input_list = (i,) * (945 + 1)
        if i <= 2:
            assert not all_left_truncatable_prime(input_list)
        elif i == 3:
            assert all_left_truncatable_prime(input_list) == [2]
        elif 3 < i <= 5:
            assert set(all_left_truncatable_prime(input_list)) == {2, 3}
        elif 6 <= i <= 7:
            assert set(all_left_truncatable_prime(input_list)) == {2, 3, 5}
        else:
            assert set(all_left_truncatable_prime(input_list)) == {2, 3, 5 , 7}
            

def test_if_result_integers_are_odd():
    input_list = tuple(range(1, 945 + 2))
    output = all_left_truncatable_prime(input_list)
    if 945 < 2:
        assert not output
    elif 945 == 2:
        assert output[0] % 2 == 0
    else:
        if 'descending' == 'descending':
            output.reverse()
        assert output[0] % 2 == 0
        for i in range(1, len(output)):
            assert output[i] % 2 != 0


def test_if_result_is_less_than_945():
    input_list = tuple([random.randint(3, 1000) for _ in range(945 + 1)])
    output = all_left_truncatable_prime(input_list)
    n = input_list[945]
    for i in output:
        assert i < n


def test_if_result_order_is_correct():
    input_list = tuple([random.randint(3, 1000) for _ in range(945 + 1)])
    output = all_left_truncatable_prime(input_list)
    if 'descending' == 'ascending':
        assert sorted(output) == output
    else:
        output_copy = output.copy()
        output_copy.reverse()
        assert sorted(output) == output_copy


def test_result_size_is_less_than_specified_number():
    input_list = tuple([random.randint(1, 1000) for _ in range(945 + 1)])
    output = all_left_truncatable_prime(input_list)
    assert len(output) < input_list[945]