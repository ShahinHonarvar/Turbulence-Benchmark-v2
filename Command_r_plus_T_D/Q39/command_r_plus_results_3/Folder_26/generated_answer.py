def return_n_greatest_chars(input_string: str) -> list[str]:
    if len(input_string) < 43:
        raise ValueError('Input string must contain at least 43 characters.')
    distinct_chars = list(set(input_string))
    distinct_chars.sort(reverse=True)
    return distinct_chars[:43]