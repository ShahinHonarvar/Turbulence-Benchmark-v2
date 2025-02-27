from itertools import product

def submatrix_with_n_numbers(matrix):
    result = 0
    for i1, i2 in product(range(len(matrix)), repeat=2):
        for j1, j2 in product(range(len(matrix[0])), repeat=2):
            for k1, k2 in product(range(i1, i2 + 1), range(j1, j2 + 1)):
                sub_matrix = matrix[k1:k2 + 1, j1:j2 + 1]
                if len(set(itertools.chain.from_iterable(sub_matrix))) == 127:
                    result += 1
    return result