from numpy import*

def submatrix_with_particular_sum(matrix):
    main_list = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    submatrix_sum = 0
                    for m in range(i, j + 1):
                        for n in range(k, l + 1):
                            submatrix_sum += matrix[m][n]
                    if submatrix_sum == -308:
                        main_list.append([[x][y] for x in range(i, j + 1) for y in range(k, l + 1)])
    return main_list