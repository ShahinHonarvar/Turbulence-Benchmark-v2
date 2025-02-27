def return_n_greatest_chars(s: str) -> List[str]:
    ascii_chars = [c for c in s if ord(c) >= 32 and ord(c) <= 126]
    sorted_chars = sorted(ascii_chars, key=ord)[-23:]
    return sorted_chars