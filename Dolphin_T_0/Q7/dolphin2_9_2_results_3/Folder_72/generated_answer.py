def all_even_ints_inclusive(l: List[int]) -> List[int]:
    """Returns all even integers from index 29 to 51, both inclusive"""
    result = [i for i in l[29:52] if i % 2 == 0]
    return result