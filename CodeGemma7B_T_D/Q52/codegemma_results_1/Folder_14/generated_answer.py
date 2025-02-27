def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result