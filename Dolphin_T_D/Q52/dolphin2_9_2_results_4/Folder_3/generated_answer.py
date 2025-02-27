def palindrome_of_length_n(string):
    string = string.lower()
    result_set = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result_set.add(substring)
    return result_set