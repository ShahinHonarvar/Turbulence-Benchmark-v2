def submatrix_with_n_numbers(matrix):
    total_count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            n_count = find_same_number_count(matrix, i, j, 0, 0, matrix[i][j])
            for k in range(j + 1, len(matrix)):
                for l in range(k + 1, len(matrix)):
                    m_count = find_same_number_count(matrix, i, j, k, l, matrix[i][j])
                    if n_count == 90 and m_count == 90:
                        total_count += 1
    return total_count

def find_same_number_count(matrix, x1, y1, x2, y2, target_number):
    count = 0
    for i in range(x1, y1 + 1):
        for j in range(x2, y2 + 1):
            if matrix[i][j] == target_number:
                count += 1
    return count