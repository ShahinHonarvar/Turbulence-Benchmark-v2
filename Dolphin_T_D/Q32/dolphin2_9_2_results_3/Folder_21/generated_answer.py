def insert_after_character(s: str) -> str:
    return ''.join(('K' if i > 0 and s[i - 1] == ' ' else s[i] for i in range(len(s))))