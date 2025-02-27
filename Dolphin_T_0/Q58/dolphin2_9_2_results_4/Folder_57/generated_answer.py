import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 92
    size_matrix = matrix.size
    indices = np.indices((matrix.shape[0], matrix.shape[1]))
    combinations = np.array(np.combinations_with_replacement(size_matrix, num_elements))
    counter = 0
    for i in range(combinations.shape[0]):
        indices_submatrix = combinations[i, :].reshape(num_elements, 1)
        entities = matrix[tuple(indices_submatrix)]
        counter += np.all(entities == entities[0])
    return counter