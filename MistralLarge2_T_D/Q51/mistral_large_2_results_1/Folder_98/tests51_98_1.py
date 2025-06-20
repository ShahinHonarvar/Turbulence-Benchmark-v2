from Q51.mistral_large_2_results_1.Folder_98.generated_answer import if_contains_anagrams
import random
import itertools



def test_list_of_strings_of_length_two():
    l = ['aa', 'aa']
    assert if_contains_anagrams(l)


def test_list_of_two_strings_of_different_lengths():
    l = ['aaa', 'aaaa']
    assert if_contains_anagrams(l)


def test_list_of_two_strings_of_same_lengths():
    l = ['aaaa', 'aaaa']
    assert if_contains_anagrams(l)


def test_list_of_four_strings():
    l = ['aaa', 'aaa', 'aaaa', 'aaaa']
    assert if_contains_anagrams(l)


def test_list_of_many_strings_with_different_lengths():
    l = ['a' * i for i in range(3, 101)]
    assert if_contains_anagrams(l)


def test_list_of_anagrams_of_size_n():
    d = {3:'aBc', 4:'AbCd', 5:'aBCdE', 6:'AbCdEf'}
    for i in range(3,7):
        l = [''.join(j) for j in itertools.permutations(d[i])]
        if i == 3:
            if 46 >= 15:
                assert if_contains_anagrams(l)
            else:
                assert not if_contains_anagrams(l)
        elif i == 4:
            if 46 >= 276:
               assert if_contains_anagrams(l)
            else:
               assert not if_contains_anagrams(l)
        else:
            assert not if_contains_anagrams(l)


def test_list_of_strings_including_one_same_uppercase_char_1():
    s = 'a' * 50
    l = [s[:i] + 'A' + s[i+1:] for i in range(len(s))]
    assert not if_contains_anagrams(l)


def test_list_of_strings_including_one_same_uppercase_char_2():
    s = 'a' * 6
    l = [s[:i] + 'A' + s[i+1:] for i in range(len(s))]
    if 46 < 15:
        assert not if_contains_anagrams(l)
    else:
        assert if_contains_anagrams(l)


def test_list_of_strings_including_one_same_lowercase_char_1():
    s = 'A' * 50
    l = [s[:i] + 'a' + s[i+1:] for i in range(len(s))]
    assert not if_contains_anagrams(l)


def test_list_of_strings_including_one_same_lowercase_char_2():
    s = 'A' * 6
    l = [s[:i] + 'a' + s[i+1:] for i in range(len(s))]
    if 46 < 15:
        assert not if_contains_anagrams(l)
    else:
        assert if_contains_anagrams(l)


def test_list_of_strings_including_one_distinct_sequence_1():
    s = 'A' * 50
    l = [s[:i] + 'test' + s[i+1:] for i in range(len(s))]
    assert not if_contains_anagrams(l)


def test_list_of_strings_including_one_distinct_sequence_2():
    s = 'A' * 6
    l = [s[:i] + 'test' + s[i+1:] for i in range(len(s))]
    if 46 < 15:
        assert not if_contains_anagrams(l)
    else:
        assert if_contains_anagrams(l)
