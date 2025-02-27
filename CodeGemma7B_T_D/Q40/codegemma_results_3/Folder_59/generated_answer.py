from functools import cmp_to_key

def return_n_smallest_chars(input_str: str) -> list[str]:
    return sorted(input_str, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)[:13]