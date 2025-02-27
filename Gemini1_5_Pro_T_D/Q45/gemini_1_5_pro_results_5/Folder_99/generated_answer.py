import string

def palindromes_between_indices(text):
    letters = set(text[4:9].lower())
    palindrome_set = set()
    for letter1 in letters.intersection(string.ascii_lowercase):
        for letter2 in letters.intersection(string.ascii_lowercase):
            for letter3 in letters.intersection(string.ascii_lowercase):
                word = letter1 + letter2 + letter3
                if len(word) >= 3 and word == word[::-1]:
                    palindrome_set.add(word)
    return palindrome_set