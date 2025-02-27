def return_nth_smallest_ascii(s: str) -> str:
    characters = [c for c in s if 8 <= s.index(c) <= 65]
    characters.sort(key=ord)
    return characters[5] if len(characters) >= 6 else ''