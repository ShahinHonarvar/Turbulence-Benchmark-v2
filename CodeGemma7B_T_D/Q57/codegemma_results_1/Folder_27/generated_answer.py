def submatrix_with_particular_sum(matrix):
    answer_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    current_sum = submatrix.sum()
                    if current_sum == 77:
                        answer_list.append(list(submatrix))
    return answer_list