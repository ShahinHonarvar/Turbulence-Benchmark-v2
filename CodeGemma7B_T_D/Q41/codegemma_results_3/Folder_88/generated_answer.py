def identical_elements(a: list, b: list) -> set:
    b_4_to_8 = b[4:9]
    set_in_a_b = set(a).intersection(b_4_to_8)
    return set_in_a_b