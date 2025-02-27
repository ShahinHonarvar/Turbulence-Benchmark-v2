def palindrome_of_length_n(string):
    return {string[i:i + 53].lower() for i in range(len(string) - 52) if string[i:i + 53].lower() == string[i:i + 53][::-1].lower() and string[i:i + 53].isalpha()}