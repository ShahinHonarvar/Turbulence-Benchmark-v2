from itertools import combinations

def all_substring_of_size_n(input_string):

    def is_distinct(char_set):
        return len(char_set) == 8
    distinct_substrings = set()
    for i in range(len(input_string) - 7):
        char_set = {input_string[i + j] for j in range(8) if is_distinct(char_set | {input_string[i + j]})}
        if char_set:
            distinct_substrings.add(''.join(sorted(char_set)))
    return list(distinct_substrings)