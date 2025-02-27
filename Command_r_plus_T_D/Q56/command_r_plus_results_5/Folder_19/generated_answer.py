from itertools import permutations

def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 17):
        substring = input_string[i:i + 18]
        if len(set(substring)) == 18:
            substrings.append(substring)
    return substrings

def all_distinct_substrings(input_string: str, n: int) -> list[str]:
    substrings = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings

def all_permutations_of_size_n(input_string: str, n: int) -> list[str]:
    unique_chars = list(set(input_string))[:n]
    all_permutations = [''.join(p) for p in permutations(unique_chars)]
    return all_permutations