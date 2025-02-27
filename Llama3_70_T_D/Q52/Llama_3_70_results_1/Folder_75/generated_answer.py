def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 79):
        if string[i:i + 80] == string[i:i + 80][::-1] and string[i:i + 80].isalpha():
            result.add(string[i:i + 80])
    return result