from Q39.gpt_4o_results_3.Folder_61.generated_answer import return_n_greatest_chars
import random
import string


def test_strings_of_size_equal_to_66():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=66))
    if 'descending' == 'ascending':
        assert return_n_greatest_chars(s) == sorted(s)
    else:
        assert return_n_greatest_chars(s) == sorted(s, reverse=True)
        

def test_length_of_result():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=66 + 1))
    assert len(return_n_greatest_chars(s)) == 66


def test_if_result_is_sorted():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=66 + 1))
    result = return_n_greatest_chars(s)
    if 'descending' == 'ascending':
        assert result == sorted(result)
    else:
        assert result == sorted(result, reverse=True)


def test_if_result_contains_highest_chars():
    selection_range = string.ascii_letters + string.digits + ' ' + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    s = ''.join(random.sample(selection_range, k=66 + 1))
    result = return_n_greatest_chars(s)
    for char_r in result:
        for char_s in s:
            if char_s not in result:
                assert char_s < char_r
            