from Q58.gpt_4o_results_4.Folder_59.generated_answer import submatrix_with_n_numbers
import random
import numpy as np
from numpy import matrix
import warnings
from functools import wraps


def ignore_warnings(f):
    @wraps(f)
    def inner(*args, **kwargs):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("ignore")
            response = f(*args, **kwargs)
        return response
    return inner


@ignore_warnings
def test_matrix_of_one_integer():
    input_matrix = [[76]]
    input_matrix = np.asmatrix(input_matrix)
    if 76 == 1:
        assert submatrix_with_n_numbers(input_matrix) == 1
    else:
        assert not submatrix_with_n_numbers(input_matrix)


@ignore_warnings
def test_matrix_of_having_76_integers():
    if 76 % 2 == 0:
        input_matrix = [[random.randint(-100, 100) for _ in range(2)] for _ in range(76 // 2)]
        input_matrix = np.asmatrix(input_matrix)
    else:
        input_matrix = [[random.randint(-100, 100) for _ in range(76)]]
        input_matrix = np.asmatrix(input_matrix)

    assert submatrix_with_n_numbers(input_matrix) == 1


@ignore_warnings
def test_horizontal_matrix():
    mat = [[random.randint(-10, 10) for _ in range(76)]]
    mat = np.asmatrix(mat)
    m = np.concatenate((mat, mat), axis=1)
    if 76 < 30:
        num = 4
    elif 30 <= 76 < 70:
        num = 3
    elif 70 <= 76 < 150:
        num = 2
    else:
        num = 1
    for i in range(num):
        m = np.concatenate((m, mat), axis=1)
        output = submatrix_with_n_numbers(m)
        expected_result = ((i + 2) * 76) + 1
        assert output == expected_result


@ignore_warnings
def test_vertical_matrix():
    m = '1 ;' * 76
    m = m[:-1]
    m = np.matrix(m)
    mat = np.concatenate((m, m), axis=0)
    if 76 < 30:
        num = 4
    elif 30 <= 76 < 70:
        num = 3
    elif 70 <= 76 < 150:
        num = 2
    else:
        num = 1
    for i in range(num):
        mat = np.concatenate((m, mat), axis=0)
        output = submatrix_with_n_numbers(mat)
        expected_result = ((i + 2) * 76) + 1
        assert output == expected_result
        