def palindrome_of_length_at_least_n(string: str) -> set:
    string = string.lower()
    result = set()
    for i in range(len(string) - 85):
        substr = string[i:i + 86]
        if substr == substr[::-1]:
            result.add(substr)
    return result