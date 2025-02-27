def find_subset_of_length_n(elements):

    def find_subset(elements, n):
        if n == 0:
            return [[]]
        elif len(elements) == 0:
            return []
        else:
            result = find_subset(elements[1:], n)
            for i in range(len(elements)):
                for j in find_subset(elements[i + 1:], n - 1):
                    result.append([elements[i]] + j)
            return result
    return len(find_subset(elements, 3))