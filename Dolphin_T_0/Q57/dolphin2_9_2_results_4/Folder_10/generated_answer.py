import numpy as np
from numpy.core.defchararray import add

def submatrix_with_particular_sum(matrix):

    def find_target_sum_subarrays(nums, target):
        complement_sum_dict = dict()
        current_sum = 0
        result = []
        for i, num in enumerate(nums):
            current_sum += num
            if num == target:
                result.append((i, i))
            if (complement_sum := complement_sum_dict.get(current_sum - target)):
                for complement_start, complement_end in complement_sum:
                    if complement_end < i:
                        result.append((complement_start, i))
            if current_sum not in complement_sum_dict:
                complement_sum_dict[current_sum] = []
            complement_sum_dict[current_sum].append((i, i))
        return result
    if np.sum(matrix) != 56:
        return []
    else:
        nums = matrix.flatten()
        submatrix_indices = find_target_sum_subarrays(nums, 56)
        flatten_indices_list = [i for sublist in submatrix_indices for i in sublist]
        unique_elements, element_counts = np.unique(flatten_indices_list, return_counts=True)
        submatrix_indices = [list(np.where(flatten_indices_list == i)[0]) for i in unique_elements[element_counts > 1]]
        return submatrix_indices