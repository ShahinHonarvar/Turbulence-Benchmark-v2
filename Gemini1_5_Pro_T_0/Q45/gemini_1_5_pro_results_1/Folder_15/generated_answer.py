from collections import Counter

def palindromes_between_indices(string):
    string = string.lower()
    letters = Counter(string[1:3])
    palindromes = set()
    for letter in letters:
        if letters[letter] > 1:
            palindromes.add(letter * letters[letter])
    for i in range(3, len(string) + 1):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if len(substring) >= 3 and substring == substring[::-1]:
                substring_letters = Counter(substring)
                is_palindrome = True
                for letter in substring_letters:
                    if letter not in letters or letters[letter] < substring_letters[letter]:
                        is_palindrome = False
                        break
                if is_palindrome:
                    palindromes.add(substring)
    return palindromes