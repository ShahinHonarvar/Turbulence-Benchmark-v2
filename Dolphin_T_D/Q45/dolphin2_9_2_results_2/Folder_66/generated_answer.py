def palindromes_between_indices(string: str) -> set:
    string = string[:6].lower()
    result = set()
    if not string:
        return result

    def helper(start_index: int, end_index: int, half_str: str, p: str) -> None:
        if end_index == len(half_str):
            result.add(p + half_str + p[::-1])
        else:
            for char in string:
                if char not in half_str:
                    helper(start_index, end_index + 1, half_str + char, p)
    half_len = len(string) // 2
    helper(0, 0, '', '')
    return result