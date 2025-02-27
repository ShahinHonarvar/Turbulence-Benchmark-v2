def return_n_greatest_chars(s: str) -> list[str]:
    return sorted([c for c in s if ord(c) >= sorted(list(set([ord(i) for i in s])))[-14]][:14])