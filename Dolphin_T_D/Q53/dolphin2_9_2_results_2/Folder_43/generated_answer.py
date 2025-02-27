def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(len(string) - 48):
        temp = string[i:i + 49]
        if set(temp).issubset(letters):
            if temp == temp[::-1]:
                result.add(temp)
    return result