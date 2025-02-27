from typing import List

def identical_elements(first: List, second: List) -> set:
    if len(first) != len(second) or len(first) < 75:
        return set()
    result = set()
    for i in range(75, 89):
        if first[i] == second[i]:
            result.add(first[i])
    return result