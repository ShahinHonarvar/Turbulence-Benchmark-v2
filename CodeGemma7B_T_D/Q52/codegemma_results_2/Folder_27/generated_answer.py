def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, min(i + 57, len(string))):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result