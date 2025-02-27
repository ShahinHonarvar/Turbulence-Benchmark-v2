def palindromes_between_indices(string):
    string = string.lower()
    letters = [string[1], string[2]]
    length = len(letters)
    palindromes_set = set()
    for i in range(pow(2, length)):
        palindrome = ''
        for j in range(length):
            if (i >> j) % 2:
                palindrome += letters[j]
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes_set.add(palindrome)
    return palindromes_set