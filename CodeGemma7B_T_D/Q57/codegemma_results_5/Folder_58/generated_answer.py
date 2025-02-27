def submatrix_with_particular_sum(matrix):
    for x1 in range(len(matrix)):
        for x2 in range(x1 + 1, len(matrix)):
            for y1 in range(len(matrix[0])):
                for y2 in range(y1 + 1, len(matrix[0])):
                    sub_matrix = matrix[x1:x2 + 1, y1:y2 + 1]
                    if sum(sub_matrix.flatten()) == -137:
                        return [[x1, y1], [x2, y2]]
    return []