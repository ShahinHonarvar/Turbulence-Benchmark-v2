def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 17):
        substring = string[i:i + 18].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result