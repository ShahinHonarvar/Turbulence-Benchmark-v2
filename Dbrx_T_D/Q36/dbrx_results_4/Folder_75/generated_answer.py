def filter_chars(s: str) -> str:
    start, end = (45, 73)
    for i in range(start, end):
        if chr(i).isalpha():
            s = s.replace(chr(i), '', end)
    return s