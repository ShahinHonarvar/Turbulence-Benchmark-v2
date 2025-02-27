import numpy as np

def submatrix_with_particular_sum(matrix):
    s = sum(matrix.flatten())
    sums = 0
    if s != 245:
        return []
    sw = [matrix[0, 0]]
    sums += sw[0]
    for i in range(matrix.shape[0]):
        if i + 1 == matrix.shape[0]:
            return []
        nw = np.append(sw, [matrix[i + 1, 0]]).astype(int)
        nw = np.delete(nw, 0)
        sums = 0
        for j in range(len(nw)):
            sums += nw[j]
            if sums > 245:
                return []
            if sums == 245:
                return [sw]
            elif j + 1 == matrix.shape[1] - 1:
                return []
    return []