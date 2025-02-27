from typing import Set

def find_original_set(sets: list[Set]) -> Set:
    result = min(sets, key=len)
    for s in sets:
        if s not in result and s.issubset(result):
            result.update(s)
    return result