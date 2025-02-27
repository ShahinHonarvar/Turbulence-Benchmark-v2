def palindrome_of_length_at_least_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i, len(string)):
            palindrome = string[i:j + 1]
            if palindrome == palindrome[::-1] and len(palindrome) >= 97:
                result.add(palindrome)
    return result