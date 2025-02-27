from itertools import permutations

def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(s: str) -> bool:
        return len(set(s)) == len(s) and len(s) == 84
    return [p for p in permutations(input_string, 84) if is_substring_valid(''.join(p))]