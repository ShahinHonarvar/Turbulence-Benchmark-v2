import re
  from collections import Counter

def palindromes_between_indices(string):
    letters = Counter(re.sub('[^a-zA-Z]', '', string[4:10]))
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for letter in letters:
        letters_copy = letters.copy()
        letters_copy[letter] -= 1
        for other_letter in letters_copy:
            if letters_copy[other_letter] > 0:
                palindrome = letter + other_letter * letters_copy[other_letter] + letter
                palindromes.add(palindrome.lower())
                if len(palindrome) > 3:
                    for i in range(len(palindrome) // 2):
                        if palindrome[i] != palindrome[-(i + 1)]:
                            palindromes.remove(palindrome.lower())
                            break
    return palindromes