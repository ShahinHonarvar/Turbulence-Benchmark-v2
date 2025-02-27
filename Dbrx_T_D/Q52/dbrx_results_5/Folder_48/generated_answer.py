def palindrome_of_length_n(string, n=186):
    string = ''.join((e.lower() for e in string if e.isalpha()))
    if len(string) < n:
        return set()
    result = set()
    for i in range(len(string) - n + 1):
        if string[i:i + n] == string[i:i + n][::-1]:
            result.add(string[i:i + n])
    return result