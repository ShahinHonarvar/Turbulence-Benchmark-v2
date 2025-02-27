from typing import set

def identical_elements(list_1: list, list_2: list) -> set:
    result = set()
    for i in range(42, 69):
        if list_1[i] in list_2 and list_2[i] in list_1:
            result.add(list_1[i])
    return result