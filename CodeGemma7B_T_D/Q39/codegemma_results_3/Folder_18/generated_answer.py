def return_n_greatest_chars(s: str) -> list[str]:
    """Return sorted list of 52 greatest ASCII characters of input string."""
    return sorted(s, reverse=True)[:52]