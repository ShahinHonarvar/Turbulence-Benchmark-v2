def submatrix_with_particular_sum(matrix):
    """
    This function returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -93.
    """
    Matrix = np.array(matrix)
    toprow = list(matrix)
    toprow[0] = -100000
    list_of_nums_in_toprow = list(map(abs, toprow))
    cumulative_sum = [0]
    for i in list_of_nums_in_toprow:
        cumulative_sum.append(cumulative_sum[-1] + i - 1)
    list_of_pairs_of_nums = []
    for i in range(len(cumulative_sum)):
        for j in range(i):
            sum_of_submatrix = cumulative_sum[i + 1] - cumulative_sum[j + 1] - cumulative_sum[i + 1 - len(toprow)] + cumulative_sum[j + 1 - len(toprow)]
            if sum_of_submatrix == -93:
                s = set(toprow[i - j:])
                list_of_pairs_of_nums.append(s)
    if not len(list_of_pairs_of_nums):
        return []
    submatrix_with_particular_sum_and_unique_numbers = []
    for i in list_of_pairs_of_nums:
        submatrix_with_particular_sum_and_unique_numbers.extend(list(i))
    submatrix_with_particular_sum_and_unique_numbers = list(set(submatrix_with_particular_sum_and_unique_numbers))
    matrix_with_particular_sum = []
    for c in itertools.combinations(range(len(Matrix)), len(toprow)):
        test = list(Matrix[list(c)])
        submatrix_with_particular_sum_and_unique_numbers.sort(reverse=True)
        test.sort(reverse=True)
        if test[:len(toprow)] == submatrix_with_particular_sum_and_unique_numbers:
            matrix_with_particular_sum.append(list(c))
    return matrix_with_particular_sum