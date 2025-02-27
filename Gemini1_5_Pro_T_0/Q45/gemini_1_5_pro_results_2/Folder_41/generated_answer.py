from collections import Counter

def palindromes_between_indices(string):
    string = string.lower()
    letters = ''
    for i in range(2, 4):
        if string[i].isalpha():
            letters += string[i]
    letters = Counter(letters)
    result = set()
    for i in range(3, len(letters) + 1):
        for combo in find_combinations(letters, i):
            if is_palindrome(combo):
                result.add(combo)
    return result

def find_combinations(letters, target_length, current_string=''):
    if target_length == 0:
        yield current_string
        return
    for letter in letters:
        if letters[letter] > 0:
            letters[letter] -= 1
            yield from find_combinations(letters, target_length - 1, current_string + letter)
            letters[letter] += 1

def is_palindrome(string):
    return string == string[::-1]