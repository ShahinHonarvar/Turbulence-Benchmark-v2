def palindrome_of_length_at_least_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 35, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result