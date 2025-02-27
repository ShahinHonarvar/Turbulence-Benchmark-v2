def submatrix_with_particular_sum(mat):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -93. If no such submatrix is found, the function should return an empty list.
    """
    '\n    # Create an empty list to store all submatrices found.\n    submatrices = []\n    '
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    submatrix_sum = sum([sum(row[j:l + 1]) for row in mat[i:k + 1]])
                    if submatrix_sum == -93:
                        submatrices.append((i, j, k, l))
    return submatrices