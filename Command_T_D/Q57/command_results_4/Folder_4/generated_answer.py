def submatrix_with_particular_sum(mat):
    result = []
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            cur_sum = 0
            for val in mat[row][col]:
                cur_sum += val
            if cur_sum == 87:
                result += [[row, col]]
    return result