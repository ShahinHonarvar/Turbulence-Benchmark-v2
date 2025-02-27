def all_substring_of_size_n(s: str) -> list[str]:
    sub_strings = []
    if len(s) < 142:
        return sub_strings
    for i in range(len(s) - 141):
        substring = s[i:i + 142]
        if len(set(substring)) == 142:
            sub_strings.append(substring)
    return sub_strings