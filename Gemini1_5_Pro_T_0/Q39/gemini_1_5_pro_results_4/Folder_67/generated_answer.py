def return_n_greatest_chars(text: str) -> list[str]:
    return sorted([c for c in text if ord(c) >= sorted(list(set([ord(i) for i in text])))[-66]])