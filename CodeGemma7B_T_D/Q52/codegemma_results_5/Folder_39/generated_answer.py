def palindrome_of_length_n(string):
    string = string.lower()
    return {substr for i in range(len(string) - 29) for j in range(i + 30, len(string)) if string[i:j] == string[j - 1:i - 1:-1]}