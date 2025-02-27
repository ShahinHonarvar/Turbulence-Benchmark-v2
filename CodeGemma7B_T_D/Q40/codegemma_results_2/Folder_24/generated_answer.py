def return_n_smallest_chars(anything: str) -> list[str]:
    assert len(set(anything)) == len(anything), 'Input must only contain unique characters'
    return sorted(anything, key=ord, reverse=True)[:32]