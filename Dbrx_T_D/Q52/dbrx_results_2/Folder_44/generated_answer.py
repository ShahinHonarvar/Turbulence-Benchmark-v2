def palindrome_of_length_n(string_arg):
    string = ''.join((e.lower() for e in string_arg if e.isalpha()))
    if len(string) < 445:
        return set()
    return {string[i:i + 445] for i in range(len(string) - 444) if string[i:i + 445] == string[i:i + 445][::-1]}