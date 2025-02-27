from itertools import combinations

def all_substring_of_size_n(s: str) -> list[str]:
    return [''.join(t) for t in combinations(s, 98) if len(set(t)) == 98]