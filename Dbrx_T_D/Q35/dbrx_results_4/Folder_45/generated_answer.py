def remove_repeat_chars(s: str) -> str:
    start, end = (40, 200)
    chars_to_remove = set(s[start:end])
    chars_to_remove = {c for c in chars_to_remove if s[start:end].count(c) > 1}
    result = [c for i, c in enumerate(s) if i < start or i >= end or c not in chars_to_remove]
    return ''.join(result)