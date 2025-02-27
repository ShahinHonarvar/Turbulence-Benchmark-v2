def return_n_greatest_chars(text: str) -> list:
    return sorted([c for c in text if ord(c) in sorted(list({ord(ch) for ch in text}))[-24:]])