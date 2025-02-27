def insert_before_character(s: str) -> str:
    return 'N'.join(('m' + i + 'N' if i == 'm' else i + 'N' for i in s)).rstrip('N')