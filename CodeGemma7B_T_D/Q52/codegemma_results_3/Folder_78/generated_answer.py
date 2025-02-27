def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 47):
        for j in range(i + 48):
            palindrome = string[i:j + 1]
            if palindrome == palindrome[::-1].lower():
                result.add(palindrome)
    return result