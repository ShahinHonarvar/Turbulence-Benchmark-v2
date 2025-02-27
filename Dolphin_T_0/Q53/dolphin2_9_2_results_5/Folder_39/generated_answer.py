def palindrome_of_length_at_least_n(string):
    s = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 68, length):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                s.add(substring)
    return s