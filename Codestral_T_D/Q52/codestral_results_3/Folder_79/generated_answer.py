def palindrome_of_length_n(string):
    string = string.lower()
    n = 64
    return {string[i:i + n] for i in range(len(string) - n + 1) if string[i:i + n] == string[i:i + n][::-1] and string[i:i + n].isalpha()}