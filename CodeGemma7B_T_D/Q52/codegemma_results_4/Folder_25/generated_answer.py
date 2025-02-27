def palindrome_of_length_n(string):
    res = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 3, len(string), 2):
            if j - i == 90 and string[i:j + 1] == string[j:i:-1]:
                res.add(string[i:j + 1])
    return res if res else set()