def find_subset_of_length_n(elements, n=45):
    return sum((1 for i in range(len(elements)) for j in range(i + 1, len(elements)) if len(elements[i:j]) == n))