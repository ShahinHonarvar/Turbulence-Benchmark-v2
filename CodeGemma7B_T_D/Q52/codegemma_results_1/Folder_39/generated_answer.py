def palindrome_of_length_n(string):
    return {palindrome for palindrome in string.casefold().split() if len(palindrome) == 59 and palindrome == palindrome[::-1]}