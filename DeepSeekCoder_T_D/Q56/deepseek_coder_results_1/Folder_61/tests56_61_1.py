from Q56.deepseek_coder_results_1.Folder_61.generated_answer import all_substring_of_size_n
import random
import string


def test_string_of_same_character():
    selection = [' ', '0', '@', 'a']
    for char in selection:
        s = ''.join(char for _ in range(1, 39 + 10))
        assert not all_substring_of_size_n(s)


def test_one_character_string():
    # Since the parameter generater (i.e. genparams.py) generates only parameters
    # of equal to or greater than 2, the answer should be an empty list.
    assert not all_substring_of_size_n('a')


def test_same_character_string():
    s = 'a' * 39
    assert not all_substring_of_size_n(s)


def test_large_string():
    if 39 < 63:
        s = ''.join(random.sample(string.ascii_letters + string.digits, k=39))
        assert all_substring_of_size_n(s) == [s]
    else:
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=39))
        assert not all_substring_of_size_n(s)


def test_length_of_substring_result():
    if 39 < 50:
        s = ''.join(random.sample(string.ascii_letters + string.digits, k=39 + 10))
    else:
        s = ''.join(random.choices(string.ascii_letters + string.digits, k=39 + 10))
    
    output = all_substring_of_size_n(s)
    for i in output:
        assert len(i) <= len(s)