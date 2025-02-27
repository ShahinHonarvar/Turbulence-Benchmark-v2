from itertools import permutations

def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(s: str) -> bool:
        return len(set(s)) == len(s) == 18
    unique_chars = set(input_string)
    valid_substrings = []
    for chars in permutations(unique_chars, 18):
        substring = ''.join(chars)
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings