def submatrix_with_n_numbers(matrix):
    count = 0
    for row, row_cells in enumerate(matrix):
        for col, cell in enumerate(row_cells):
            if cell + row + col == 176:
                count += 1
    return count