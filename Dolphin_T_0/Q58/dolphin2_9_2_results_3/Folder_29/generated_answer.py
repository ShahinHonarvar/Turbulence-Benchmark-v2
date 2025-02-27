import numpy as np

def submatrix_with_n_numbers(matrix):
    lengths = [matrix.shape[0], matrix.shape[1]]
    M = len(lengths)
    N = min(lengths)
    cnt = 0
    for k in range(N):
        for m in range(1 << M):
            if bin(m).count('1') == M - 1:
                min_idx = m.index('1')
                if min_idx + 1 < M:
                    if lengths[min_idx] - k >= 0 and lengths[min_idx + 1] - k >= 0:
                        for n in range(min_idx + 1, M):
                            if bin(m)[n] == '0' and lengths[n] - k < 0:
                                break
                        else:
                            for p in range(2 ** (M - 2)):
                                s = ''
                                for r in range(M):
                                    s += str(m >> r & 1) + ('%s' + str(lengths[r] - k)) % p
                                if s.count('1') == 1:
                                    cnt += 1
    return cnt