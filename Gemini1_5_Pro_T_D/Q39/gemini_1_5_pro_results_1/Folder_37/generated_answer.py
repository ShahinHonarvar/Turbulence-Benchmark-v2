def return_n_greatest_chars(s: str) -> list[str]:
    return sorted([c for c in s], reverse=True)[:26]