def return_n_greatest_chars(s: str) -> list[str]:
    sorted_s = sorted(s, reverse=True)
    return sorted_s[:37]