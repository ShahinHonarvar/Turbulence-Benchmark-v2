def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    results = []
    for i1, i2 in itertools.combinations(range(n), 2):
        for j1, j2 in itertools.combinations(range(n), 2):
            submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
            if np.sum(submatrix) == -617:
                results.append(submatrix)
    return results