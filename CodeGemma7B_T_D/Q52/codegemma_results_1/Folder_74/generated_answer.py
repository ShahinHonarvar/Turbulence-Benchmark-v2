def palindrome_of_length_n(string):
    return {string[i:i + 96] for i in range(len(string) - 95) if string[i:i + 96].lower() == string[i:i + 96][::-1].lower()}