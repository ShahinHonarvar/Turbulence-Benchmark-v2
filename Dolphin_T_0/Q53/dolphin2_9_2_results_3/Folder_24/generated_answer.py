def palindrome_of_length_at_least_n(string):
    result = set()
    if not isinstance(string, str):
        return result
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 52, len(string)):
            substring = string[i:j + 1]
            if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substring)) and substring == substring[::-1]:
                result.add(substring)
    return result