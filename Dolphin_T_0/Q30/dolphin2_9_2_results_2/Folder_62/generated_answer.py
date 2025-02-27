def insert_before_character(string: str) -> str:
    return 'o' + string if not string else 'o' + string[0] + 'o'.join([string[i] + string[i + 1] for i in range(len(string) - 1) if string[i] == ' '])