from Q32.command_r_plus_results_5.Folder_6.generated_answer import insert_after_character
import random
import string


def test_string_of_length_one():
    s = 'X'
    assert insert_after_character(s) == 'X' + 'u'


def test_large_string_of_only_specified_character():
    s = 'X' * 1000
    assert insert_after_character(s) == ('X' + 'u') * 1000


def test_length_of_large_string_of_only_specified_character():
    s = 'X' * 1000
    assert len(insert_after_character(s)) == 2 * len(s)


def test_presence_of_inserted_character():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k = 1000))
    s = s + 'X'
    returned_string = insert_after_character(s)
    assert 'u' in returned_string


def test_compare_length_of_strings():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'X'
    returned_string = insert_after_character(s)
    assert len(s) < len(returned_string)
    

def test_length_of_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'X'
    returned_string = insert_after_character(s)
    count = s.count('X')
    assert len(returned_string) == len(s) + count
    

def test_first_index_of_insert_char_in_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s.replace('u', '')
    s = s.replace('X', '')
    s = 'X' + s
    returned_string = insert_after_character(s)
    if 'u' == 'X':
        assert returned_string.find('u') == 0
        assert returned_string.rfind('u') == 1
    else:
        assert returned_string.find('u') == 1


def test_all_indices_of_char_destination_in_result():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + 'X'
    s = s.replace('u', '')
    returned_string = insert_after_character(s)
    indices_in_s = [i[0] for i in enumerate(s) if i[1] == 'X']
    indices_in_returned_string = [i[0] for i in enumerate(returned_string) if i[1] == 'u']
    length = len(indices_in_s)
    assert length == len(indices_in_returned_string)
    l = [indices_in_s[i] + i + 1 for i in range(len(indices_in_s))]
    assert l == indices_in_returned_string
