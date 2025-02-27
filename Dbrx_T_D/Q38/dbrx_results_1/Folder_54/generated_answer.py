def find_subset_of_length_n(elements: set, n: int=51) -> int:
    subsets = [set() for _ in range(n)]
    for i in range(n - 1):
        for element in elements.difference(subsets[i]):
            subsets[i + 1].add(element)
        subsets[i + 1].update(subsets[i])
    return sum((1 for subset in subsets if len(subset) == n))