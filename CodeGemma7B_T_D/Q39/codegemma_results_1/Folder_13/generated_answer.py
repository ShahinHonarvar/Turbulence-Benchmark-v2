def return_n_greatest_chars(chars):
    assert len(chars) >= 31
    return sorted(chars)[-31:]