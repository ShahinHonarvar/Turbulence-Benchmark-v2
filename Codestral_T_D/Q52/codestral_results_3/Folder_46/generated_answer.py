def palindrome_of_length_n(string):
    string = string.lower()
    length = 464
    return {string[i:i + length] for i in range(len(string) - length + 1) if string[i:i + length] == string[i:i + length][::-1] and string[i:i + length].isalpha()}