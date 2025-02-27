def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 113):
        string = s[i:i + 113]
        if string == string[::-1] and set(string).issubset('abcdefghijklmnopqrstuvwxyz'):
            result.add(string)
    return result