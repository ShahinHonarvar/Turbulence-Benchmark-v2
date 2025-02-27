from collections import defaultdict

def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            word = string[i:j + 1].lower()
            if word == word[::-1]:
                result.add(word)
    return result