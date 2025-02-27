def submatrix_with_n_numbers(matrix):
    return len(np.where((matrix == 0) == False)[0][np.where((matrix == 93) == True)[0]])