def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 317):
        substring = string[i:i + 318].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result