from Q40.mistral_large_2_results_3.Folder_56.generated_answer import return_n_smallest_chars
import random
import string


def test_strings_of_size_equal_to_21():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=21))
    if 'ascending' == 'ascending':
        assert return_n_smallest_chars(s) == sorted(s)
    else:
        assert return_n_smallest_chars(s) == sorted(s, reverse=True)


def test_length_of_result():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=21 + 1))
    assert len(return_n_smallest_chars(s)) == 21


def test_if_result_is_sorted():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=21 + 1))
    result = return_n_smallest_chars(s)
    if 'ascending' == 'ascending':
        assert result == sorted(result)
    else:
        assert result == sorted(result, reverse=True)


def test_if_result_contains_highest_chars():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=21 + 1))
    result = return_n_smallest_chars(s)
    for char_r in result:
        for char_s in s:
            if char_s not in result:
                assert char_r < char_s
                            