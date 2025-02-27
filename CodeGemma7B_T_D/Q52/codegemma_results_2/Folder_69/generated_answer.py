def palindrome_of_length_n(string):
    low_case_string = string.lower()
    result = set()
    for i in range(len(low_case_string) - 471):
        for j in range(i + 472):
            substring = low_case_string[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result