def all_substring_of_size_n(str_: str) -> list[str]:
    result = []
    for i in range(len(str_) - 47):
        substring = str_[i:i + 48]
        if len(set(substring)) == 48:
            result.append(substring)
    return result