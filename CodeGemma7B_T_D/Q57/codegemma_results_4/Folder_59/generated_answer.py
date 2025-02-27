def submatrix_with_particular_sum(matrix):
    """
    Write a function called 'submatrix_with_particular_sum' that takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 2. If no such submatrix is found, the function should return an empty list.
    """

    def submatrix_sum(matrix, lt, rb):
        sum = 0
        for i in range(lt[0], rb[0] + 1):
            for j in range(lt[1], rb[1] + 1):
                sum += matrix[i][j]
        return sum
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if submatrix_sum(matrix, (row_start, col_start), (row_end, col_end)) == 2:
                        result.append((row_start, col_start, row_end, col_end))
    return result