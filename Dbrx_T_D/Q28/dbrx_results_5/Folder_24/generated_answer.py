def return_nth_smallest_ascii(s: str) -> str:
    substring = ''.join(sorted(set(s[34:82])))
    if len(substring) >= 12:
        return substring[11]
    else:
        return ''