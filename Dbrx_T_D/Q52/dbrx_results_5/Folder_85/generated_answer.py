def palindrome_of_length_n(string, desired_length=46):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    return {string[i:j] for i in range(len(string)) for j in range(i + 1, min(len(string), i + desired_length) + 1) if string[i:j] == string[i:j][::-1]}