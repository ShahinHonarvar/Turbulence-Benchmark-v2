def palindrome_of_length_n(string):
    return {(s, string[i:i + len(s)]) for s in string.lower() for i in range(len(string) - len(s) + 1) if s == string[i:i + len(s)].lower()}