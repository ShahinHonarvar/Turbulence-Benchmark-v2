from Q55.deepseek_coder_results_2.Folder_52.generated_answer import lists_with_product_equal_n
import random
import math


def test_list_of_single_number():
    assert lists_with_product_equal_n([37]) == [[37]]


def test_presence_of_duplicates_in_result():
    input_list = [1, 37, 1, 37, 1, 37]
    result = lists_with_product_equal_n(input_list)
    if 37 == 0:
        assert result.count([0]) == 3 and result.count([1, 0]) == 3 and result.count([0, 1]) == 3 and result.count(
        [1, 0, 1]) == 3 and result.count([0, 1, 0]) == 3 and result.count([1, 0, 1, 0]) == 3 and result.count(
        [0, 1, 0, 1]) == 3 and result.count([0, 1, 0, 1, 0]) == 3 and result.count(
        [1, 0, 1, 0, 1]) == 3 and result.count([1, 0, 1, 0, 1, 0]) == 3 and result.count([0, 1, 0, 1, 0, 1]) == 3
    elif 37 == 1:
        assert result.count([37]) == 6 and result.count([1, 37]) == 6 and result.count([37, 1]) == 6 and result.count([1, 37, 1]) == 6
    else:
        assert result.count([37]) == 3 and result.count([1, 37]) == 3 and result.count([37, 1]) == 3 and result.count([1, 37, 1]) == 3


def test_list_of_several_same_number():
    n = random.randint(1,100)
    l = []
    if 37 == 0 or 37 == 1:
        for i in range(1, n + 1):
            l.append([37] * i)
        l = l * n  
    elif 37 == -1:
        for i in range(1, n + 1):
            if i % 2 != 0:
                l.append([-1] * i)
        l = l * n
    else:
        l = [[37]] * n

    input_list = [37] * n
    assert lists_with_product_equal_n(input_list) == l


def test_list_of_not_containing_number():
    n = 37
    while n == 37:
        n = random.randint(-1000,1001)
    
    assert not lists_with_product_equal_n([n])


def test_sublist_size():
    if 37 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))

    elif 37 > 0:
        divs = [i for i in range(1, 37 + 1) if 37 % i == 0]
        input_list = divs + divs

    else:
        n = -37
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs
    
    result = lists_with_product_equal_n(input_list)
    length = len(input_list)
    for i in result:
        assert len(i) <= length


def test_return_elements_are_in_given_list():
    input_list = []
    if 37 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif 37 > 0:
        divs = [i for i in range(1, 37 + 1) if 37 % i == 0]
        input_list = divs + divs
    else:
        n = -37
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            for i in r:
                assert i in input_list


def test_if_sublist_product_equals_number():
    input_list = []
    if 37 == 0:
        k = random.randint(1, 4)
        input_list = list(range(-k, k + 1))
    elif 37 > 0:
        divs = [i for i in range(1, 37 + 1) if 37 % i == 0]
        input_list = divs + divs
    else:
        n = -37
        divs = [-i for i in range(1, n + 1) if n % i == 0]
        input_list = divs + divs

    result = lists_with_product_equal_n(input_list)
    if result:
        for r in result:
            assert math.prod(r) == 37
