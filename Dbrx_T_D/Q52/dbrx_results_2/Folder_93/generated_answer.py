import re

def palindrome_of_length_n(string, n=45):
    palindrome_set = set()
    string = re.sub('[^a-zA-Z]', '', string).lower()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    if len(palindrome_set) == 0:
        return 'No palindromes of length 45 in the given string'
    else:
        return palindrome_set