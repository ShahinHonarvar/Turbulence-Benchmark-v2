def palindrome_of_length_at_least_n(string):
    return {palindrome.lower(): palindrome for palindrome in string.split() if len(palindrome) >= 59 and palindrome.isalpha()}