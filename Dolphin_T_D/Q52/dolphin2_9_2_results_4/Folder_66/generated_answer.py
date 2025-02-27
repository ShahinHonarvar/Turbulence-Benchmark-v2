def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 24):
        temp = string[i:i + 25]
        if temp == temp[::-1]:
            result.add(temp)
    return result