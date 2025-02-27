def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix)):
                    if len(set(flatten(matrix[i:k + 1][j:l + 1]))) == 78:
                        count += 1
    return count

def flatten(matrix):
    return [item for row in matrix for item in row]