from itertools import combinations

def submatrix_with_particular_sum(matrix):
    """
    This function takes one argument which is a two-dimensional numpy matrix of integers. The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 87. If no such submatrix is found, the function should return an empty list.
    """

    def get_submatrix(matrix, row1, col1, row2, col2):
        """
        This function takes a matrix and two row and column indices as arguments and returns a submatrix of the given matrix starting from the top-left corner at (row1, col1) to bottom-right corner at (row2, col2).
        """
        submatrix = []
        for row in range(row1, row2 + 1):
            submatrix.append(matrix[row][col1:col2 + 1])
        return submatrix

    def get_sum_of_submatrix(submatrix):
        """
        This function takes a submatrix as an argument and returns the sum of all integers in the submatrix.
        """
        sum = 0
        for row in submatrix:
            for col in row:
                sum += col
        return sum
    rows = range(len(matrix))
    cols = range(len(matrix[0]))
    combinations_list = list(combinations(rows, 2)) + list(combinations(cols, 2))
    submatrices = []
    for row1, row2 in combinations_list:
        for col1, col2 in combinations_list:
            if row1 <= row2 and col1 <= col2:
                submatrix = get_submatrix(matrix, row1, col1, row2, col2)
                if get_sum_of_submatrix(submatrix) == 87:
                    submatrices.append(submatrix)
    return submatrices