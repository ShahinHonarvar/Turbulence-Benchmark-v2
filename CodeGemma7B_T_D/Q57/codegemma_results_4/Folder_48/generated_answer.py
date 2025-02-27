def submatrix_with_particular_sum(matrix):
    answer_list = []
    submat_size = len(matrix)
    for ki in range(0, submat_size):
        for kj in range(0, submat_size):
            for mi in range(0, submat_size):
                for mj in range(0, submat_size):
                    current_sum = 0
                    current_sub = []
                    for i in range(ki, mi + 1):
                        for j in range(kj, mj + 1):
                            current_sum += matrix[i][j]
                            current_sub.append(matrix[i][j])
                    if current_sum == -261:
                        answer_list.append(current_sub)
    return answer_list