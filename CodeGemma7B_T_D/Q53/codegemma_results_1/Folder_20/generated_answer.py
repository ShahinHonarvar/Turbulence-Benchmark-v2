def palindrome_of_length_at_least_n(string: str) -> set[str]:
    _set = set()
    for start in range(len(string)):
        for end in range(start + 66, len(string) + 1):
            substring = string[start:end]
            if substring == substring[::-1]:
                _set.add(substring)
    return _set