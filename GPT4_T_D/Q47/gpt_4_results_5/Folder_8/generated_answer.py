import re

def palindromes_of_specific_lengths(my_string):
    substr = my_string[17:73]
    result = set()
    for i in range(len(substr)):
        for j in range(i + 50, min(i + 52, len(substr) + 1)):
            potential_palindrome = substr[i:j]
            if potential_palindrome == potential_palindrome[::-1]:
                potential_palindrome = re.sub('[^a-z]', '', potential_palindrome.lower())
                if len(potential_palindrome) >= 50:
                    result.add(potential_palindrome)
    return result