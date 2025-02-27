def palindrome_of_length_n(str):
    result = set()
    low_str = str.lower()
    for i in range(len(low_str)):
        for j in range(i, len(low_str)):
            substring = low_str[i:j + 1]
            if substring == substring[::-1] and len(substring) == 7:
                result.add(substring)
    return result