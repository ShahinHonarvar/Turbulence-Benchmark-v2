from collections import Counter

def palindromes_between_indices(string):
    string = string[1:5].lower()
    letters = [letter for letter in string if letter.isalpha()]
    if len(letters) < 4:
        return set()
    palindrome_set = set()
    for i in range(len(letters) - 3):
        for j in range(i + 1, len(letters) - 2):
            for k in range(j + 1, len(letters)):
                for letter4 in letters:
                    if i != j and j != k and (i != k):
                        test_string = letters[i] + letters[j] + letters[k] + letter4
                        if test_string == test_string[::-1]:
                            palindrome_set.add(test_string)
    return palindrome_set