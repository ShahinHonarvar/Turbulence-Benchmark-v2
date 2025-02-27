def return_n_greatest_chars(text: str) -> list[str]:
    return sorted([char for char in text], reverse=True)[:26]