import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_sum(arr, target_sum):
        submatrices = []
        for top in range(len(arr)):
            temp = np.zeros(len(arr[0]))
            for bottom in range(top, len(arr)):
                temp += arr[bottom]
                current_sum = 0
                sum_dict = {0: [-1]}
                for right in range(len(arr[0])):
                    current_sum += temp[right]
                    if current_sum - target_sum in sum_dict:
                        for start_col in sum_dict[current_sum - target_sum]:
                            submatrices.append(arr[top:bottom + 1, start_col + 1:right + 1].tolist())
                    if current_sum in sum_dict:
                        sum_dict[current_sum].append(right)
                    else:
                        sum_dict[current_sum] = [right]
        return submatrices
    return find_submatrix_sum(matrix, -90)