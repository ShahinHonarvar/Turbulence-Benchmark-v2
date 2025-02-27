def palindrome_of_length_n(string):
    string = ''.join((e for e in string.upper() if e.isalpha()))
    length = 13
    if length > len(string) or length < 0:
        return set()
    result = set()
    for i in range(len(string) - length + 1):
        if string[i:i + length] == string[i:i + length][::-1]:
            result.add(string[i:i + length])
    return result