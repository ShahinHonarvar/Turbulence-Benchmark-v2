from Q40.command_r_plus_results_1.Folder_57.generated_answer import return_n_smallest_chars
import random
import string


def test_strings_of_size_equal_to_29():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=29))
    if 'descending' == 'ascending':
        assert return_n_smallest_chars(s) == sorted(s)
    else:
        assert return_n_smallest_chars(s) == sorted(s, reverse=True)


def test_length_of_result():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=29 + 1))
    assert len(return_n_smallest_chars(s)) == 29


def test_if_result_is_sorted():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=29 + 1))
    result = return_n_smallest_chars(s)
    if 'descending' == 'ascending':
        assert result == sorted(result)
    else:
        assert result == sorted(result, reverse=True)


def test_if_result_contains_highest_chars():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=29 + 1))
    result = return_n_smallest_chars(s)
    for char_r in result:
        for char_s in s:
            if char_s not in result:
                assert char_r < char_s
                            