def filter_chars(s: str) -> str:
    unwanted_chars = [chr(i) for i in range(69, 73)]
    return ''.join([char for char in s if char not in unwanted_chars])