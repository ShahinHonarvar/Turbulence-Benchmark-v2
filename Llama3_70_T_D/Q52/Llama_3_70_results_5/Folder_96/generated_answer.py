def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 82):
        substring = string[i:i + 83]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result