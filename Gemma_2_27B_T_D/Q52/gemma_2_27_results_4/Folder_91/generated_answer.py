def palindrome_of_length_n(string):
    return {string[i:i + 7].lower() for i in range(len(string) - 6) if string[i:i + 7].lower() == string[i + 6:i:-1].lower()}