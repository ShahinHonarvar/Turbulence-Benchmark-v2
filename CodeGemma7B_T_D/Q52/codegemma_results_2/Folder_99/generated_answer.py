def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) == 420 and substring.isalpha():
                result.add(substring.lower())
    return result