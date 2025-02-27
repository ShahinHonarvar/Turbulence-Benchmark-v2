def return_nth_smallest_ascii(s: str) -> str:
    characters = sorted((s[i] for i in range(len(s)) if 37 <= i <= 59))
    return characters[6] if len(characters) > 6 else None