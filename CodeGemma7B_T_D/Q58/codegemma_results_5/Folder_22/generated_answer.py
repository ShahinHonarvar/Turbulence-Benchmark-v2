def submatrix_with_n_numbers(matrix):
    """
    :param matrix: is a 2-d numpy matrix of integers
    :return: count of submatrices with 21 integers
    """
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 20 < len(matrix):
                a = set()
                for k in range(i, i + 21):
                    a.add(tuple(matrix[k][j:j + 21]))
                if len(a) == 1:
                    count += 1
            if j + 20 < len(matrix[0]):
                a = set()
                for k in range(j, j + 21):
                    a.add(tuple(matrix[i:i + 21][k]))
                if len(a) == 1:
                    count += 1
            if i + 20 < len(matrix) and j + 20 < len(matrix[0]):
                a = set()
                for k in range(i, i + 21):
                    for l in range(j, j + 21):
                        a.add(matrix[k][l])
                if len(a) == 21:
                    count += 1
            if i + 20 < len(matrix) and j - 20 >= 0:
                a = set()
                for k in range(i, i + 21):
                    for l in range(j - 20, j + 1):
                        a.add(matrix[k][l])
                if len(a) == 21:
                    count += 1
    return count