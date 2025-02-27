def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 48):
        sub = string[i:i + 49]
        if sub == sub[::-1]:
            result.add(sub)
    return result