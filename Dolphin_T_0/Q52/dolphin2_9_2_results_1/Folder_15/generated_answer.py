def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 4 and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result