from Q33.claude_3_5_haiku_results_4.Folder_37.generated_answer import return_vowels
import string
import random


def test_repeat_consonant_char():
    s = 'm' * (90 + 2)
    assert not return_vowels(s)
   

def test_distinct_consonant_chars():
    s = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    assert not return_vowels(s)


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(90*100))
    assert len(return_vowels(s)) <= len(s)


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(90*2))
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    returned_s = return_vowels(s)
    sliced_s = s[82:90]
    for char in sliced_s:
        if char in vowels and 'T' < char <= 'b':
            assert char in returned_s


def test_no_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82)) + 'd' * (90-82) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))

    assert not return_vowels(s)


def test_all_vowels_in_range():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(82)) + 'i' * (90-82) + ''.join(
    random.choice(string.ascii_letters) for _ in range(10))
    
    if 'T' < 'i' <= 'b':
        assert return_vowels(s) == ['i' for _ in range(90-82)]
    else:
        assert not return_vowels(s)
        