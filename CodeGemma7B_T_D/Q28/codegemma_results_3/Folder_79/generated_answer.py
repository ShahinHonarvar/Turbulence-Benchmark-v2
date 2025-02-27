from functools import cmp_to_key

def return_nth_smallest_ascii(string: str) -> str:
    return sorted(filter(lambda char: 13 <= string.index(char) <= 35, string), key=cmp_to_key(lambda x, y: ord(x) - ord(y)))[17]