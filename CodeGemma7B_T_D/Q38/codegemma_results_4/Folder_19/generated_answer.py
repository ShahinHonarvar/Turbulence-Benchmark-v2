def find_subset_of_length_n(set_of_elements):
    answer = 0
    for subset in itertools.combinations(set_of_elements, 13):
        answer += 1
    return answer