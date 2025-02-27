from numpy import*

def submatrix_with_particular_sum(matrix):
    size = len(matrix)
    result = []
    for x in range(size):
        for y in range(size):
            for w in range(x + 1, size + 1):
                for h in range(y + 1, size + 1):
                    if sum(matrix[x:w, y:h].flatten()) == -47:
                        sub_matrix = [matrix[i][j] for i in range(x, w) for j in range(y, h)]
                        result.append(sub_matrix)
    return result