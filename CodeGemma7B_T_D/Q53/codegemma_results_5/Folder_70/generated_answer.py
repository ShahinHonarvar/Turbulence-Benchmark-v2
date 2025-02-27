def palindrome_of_length_at_least_n(str):
    result = set()
    for i in range(len(str)):
        for j in range(i + 11, len(str) + 1):
            palindrome = str[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result