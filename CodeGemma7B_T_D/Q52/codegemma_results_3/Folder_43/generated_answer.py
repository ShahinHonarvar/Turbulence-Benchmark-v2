from re import sub

def palindrome_of_length_n(arg):
    return {word for word in sub('[^a-z]', '', arg.lower()).split() if len(word) == 34}