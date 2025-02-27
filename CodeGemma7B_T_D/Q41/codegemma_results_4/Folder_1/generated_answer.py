from itertools import product

def identical_elements(A: list[int], B: list[int]) -> set[int]:
    """
            Combines two lists and discards all elements outside of the specified index range.
            """
    return set((b for a, b in product(A, B) if 31 <= a <= 72 and 31 <= b <= 72))